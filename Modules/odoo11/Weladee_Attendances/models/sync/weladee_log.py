# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import time
import datetime

from odoo.addons.Weladee_Attendances.models.grpcproto import odoo_pb2
from odoo.addons.Weladee_Attendances.models.grpcproto import weladee_pb2
from .weladee_base import stub, sync_loginfo, sync_logerror, sync_logdebug

def sync_log_data(emp_obj, att_line_obj, weladee_att, odoo_weladee_ids, context_sync):
    '''
    sync log data from weladee to odoo data

    1 odoo record will link 2 weladee logevent

    '''
    ret = {'mode':'',
           'res-id':0,
           'employee_id': odoo_weladee_ids.get(str(weladee_att.logevent.employeeid),False)}

    date = datetime.datetime.fromtimestamp(weladee_att.logevent.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    if weladee_att.odoo and weladee_att.odoo.odoo_id:
       sync_logdebug(context_sync, 'has link for weladee-odoo')
       att_rec = att_line_obj.browse(weladee_att.odoo.odoo_id)
       if att_rec:
          ret['mode'] = 'update' 
          ret['res-id'] = weladee_att.odoo.odoo_id

       else:
          sync_logerror(context_sync, 'Not found this id %s in odoo' % weladee_att.odoo.odoo_id)
    else:
       #new link
       ret['mode'] = 'create'
    
    #manage data
    if weladee_att.logevent.action == "i" :
       ret["check_in"] = date

    elif weladee_att.logevent.action == "o" :
        ret["check_out"] = date
        prev_rec = att_line_obj.search( [ ('employee_id','=', ret['employee_id'] ), ('check_out','=', False)] )
        if prev_rec:
           ret['mode'] = 'update' 
           ret['res-id'] = prev_rec.id
        elif ret['mode'] == 'create':
          ret['mode'] = ''
          sync_logerror(context_sync, 'check in of employee %s not found' % ret['employee_id'])

    return ret      

def get_emp_odoo_weladee_ids(emp_obj, odoo_weladee_ids):
    '''
    return odoo id from weladee id
    '''
    odoo_weladee_ids = {}
    for each in emp_obj.search([('weladee_id','!=',False),'|',('active','=',False),('active','=',True)]):
        odoo_weladee_ids[each.weladee_id] = each.id

    return odoo_weladee_ids    

def sync_log(emp_obj, att_line_obj, authorization, context_sync):
    '''
    sync all log from weladee

    '''
    iteratorAttendance = []
    odoo_weladee_ids = {}
    try:
        sync_loginfo(context_sync, 'updating changes from weladee-> odoo')
        for att in stub.GetNewAttendance(weladee_pb2.Empty(), metadata=authorization):
            if att and att.logevent:

               #if empty, create one 
               if not odoo_weladee_ids: 
                  sync_logdebug(context_sync, 'getting all employee-weladee link') 
                  odoo_weladee_ids = get_emp_odoo_weladee_ids(emp_obj, odoo_weladee_ids)

               odoo_log = sync_log_data(emp_obj, att_line_obj, att, odoo_weladee_ids, context_sync)

               if odoo_log and odoo_log['mode'] == 'create':
                  attendace_odoo_id = att_line_obj.create(odoo_log) 
                  #update record to weladee
                  syncLogEvent = odoo_pb2.LogEventOdooSync()
                  syncLogEvent.odoo.odoo_id = attendace_odoo_id.id
                  syncLogEvent.odoo.odoo_created_on = int(time.time())
                  syncLogEvent.odoo.odoo_synced_on = int(time.time())
                  syncLogEvent.logid = att.logevent.id
                  iteratorAttendance.append(syncLogEvent)

               elif odoo_log and odoo_log['mode'] == 'update':
                  oldrec = att_line_obj.browse(odoo_log['res-id'])
                  if oldrec:
                     oldrec.write(odoo_log)
                     #update record to weladee
                     syncLogEvent = odoo_pb2.LogEventOdooSync()
                     syncLogEvent.odoo.odoo_id = oldrec.id
                     syncLogEvent.odoo.odoo_created_on = int(time.time())
                     syncLogEvent.odoo.odoo_synced_on = int(time.time())
                     syncLogEvent.logid = att.logevent.id
                     iteratorAttendance.append(syncLogEvent)
                  else:
                    sync_logerror(context_sync, 'Not found this id %s in odoo' % odoo_log['res-id'])
            else:
                sync_logdebug(context_sync, 'no log event') 

    except Exception as e:
        sync_logerror(context_sync, 'error while updating log %s' % e)

    if len( iteratorAttendance ) > 0 :
        ge = generators(iteratorAttendance)
        __ = stub.SyncAttendance( ge , metadata=authorization )
    else:
        sync_logerror(context_sync, 'No data to sent')

def generators(iteratorAttendance):
    for i in iteratorAttendance :
        yield i