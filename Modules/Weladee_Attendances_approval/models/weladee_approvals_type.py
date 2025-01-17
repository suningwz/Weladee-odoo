# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class weladee_approvals_type(models.Model):
    _inherit = 'fw.approvals.type'
    _sql_constraints = [
        ('unique_approval_type_name', 'UNIQUE(name,weladee_id)', _('Approval type name must be unique.')),
    ]

    weladee_id = fields.Char(string="Weladee ID",copy=False, default="", readonly=True, required=True)
    weladee_url = fields.Char(string="Weladee Url", copy=False, default="", readonly=True, required=True)

    @api.model
    def create(self, vals):
        if 'res-mode' in vals:
            del vals['res-mode']
        return super(weladee_approvals_type, self).create(vals)

    def write(self, vals):
        if self.weladee_id and 'res-mode' not in vals and 'res-id' not in vals:
            raise UserError(_('This approval type can only be edited on Weladee.'))
        if 'res-mode' in vals:
            del vals['res-mode']
        if 'res-id' in vals:
            del vals['res-id']
        return super(weladee_approvals_type, self).write(vals)
    
    def open_weladee_approvals_type(self):
        if self.weladee_url:
            return {
                'name': _('Approval Type'),
                'type': 'ir.actions.act_url',
                'url': self.weladee_url,
                'target': 'new'
            }
        else:
            raise UserError(_("This approval type don't have a weladee id."))
