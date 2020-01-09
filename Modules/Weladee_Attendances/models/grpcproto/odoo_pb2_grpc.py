# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import odoo_pb2 as odoo__pb2
from . import weladee_pb2 as weladee__pb2


class OdooStub(object):
  """*
  List of available functions for Odoo only.
  Don't forget to authenticate yourself with metadata "authorization" with api_key
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateEmployee = channel.unary_unary(
        '/grpc.weladee.com.Odoo/UpdateEmployee',
        request_serializer=odoo__pb2.EmployeeOdoo.SerializeToString,
        response_deserializer=weladee__pb2.Empty.FromString,
        )
    self.GetEmployees = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetEmployees',
        request_serializer=odoo__pb2.OdooRequest.SerializeToString,
        response_deserializer=odoo__pb2.EmployeeOdoo.FromString,
        )
    self.AddEmployee = channel.unary_unary(
        '/grpc.weladee.com.Odoo/AddEmployee',
        request_serializer=odoo__pb2.EmployeeOdoo.SerializeToString,
        response_deserializer=weladee__pb2.AddResult.FromString,
        )
    self.GetEmployeeHolidays = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetEmployeeHolidays',
        request_serializer=odoo__pb2.OdooRequest.SerializeToString,
        response_deserializer=odoo__pb2.HolidayOdoo.FromString,
        )
    self.GetHolidays = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetHolidays',
        request_serializer=weladee__pb2.Empty.SerializeToString,
        response_deserializer=odoo__pb2.HolidayOdoo.FromString,
        )
    self.AddHoliday = channel.unary_unary(
        '/grpc.weladee.com.Odoo/AddHoliday',
        request_serializer=odoo__pb2.HolidayOdoo.SerializeToString,
        response_deserializer=weladee__pb2.AddResult.FromString,
        )
    self.DropHoliday = channel.unary_unary(
        '/grpc.weladee.com.Odoo/DropHoliday',
        request_serializer=odoo__pb2.OdooRequest.SerializeToString,
        response_deserializer=weladee__pb2.Empty.FromString,
        )
    self.UpdateHoliday = channel.unary_unary(
        '/grpc.weladee.com.Odoo/UpdateHoliday',
        request_serializer=odoo__pb2.HolidayOdoo.SerializeToString,
        response_deserializer=weladee__pb2.Empty.FromString,
        )
    self.GetDepartments = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetDepartments',
        request_serializer=odoo__pb2.OdooRequest.SerializeToString,
        response_deserializer=odoo__pb2.DepartmentOdoo.FromString,
        )
    self.AddDepartment = channel.unary_unary(
        '/grpc.weladee.com.Odoo/AddDepartment',
        request_serializer=odoo__pb2.DepartmentOdoo.SerializeToString,
        response_deserializer=weladee__pb2.AddResult.FromString,
        )
    self.UpdateDepartment = channel.unary_unary(
        '/grpc.weladee.com.Odoo/UpdateDepartment',
        request_serializer=odoo__pb2.DepartmentOdoo.SerializeToString,
        response_deserializer=weladee__pb2.Empty.FromString,
        )
    self.GetNewAttendance = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetNewAttendance',
        request_serializer=odoo__pb2.AttendanceRequest.SerializeToString,
        response_deserializer=odoo__pb2.LogEventOdoo.FromString,
        )
    self.GetPositions = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetPositions',
        request_serializer=weladee__pb2.Empty.SerializeToString,
        response_deserializer=odoo__pb2.PositionOdoo.FromString,
        )
    self.AddPosition = channel.unary_unary(
        '/grpc.weladee.com.Odoo/AddPosition',
        request_serializer=odoo__pb2.PositionOdoo.SerializeToString,
        response_deserializer=weladee__pb2.AddResult.FromString,
        )
    self.GetProjects = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetProjects',
        request_serializer=weladee__pb2.Empty.SerializeToString,
        response_deserializer=odoo__pb2.ProjectOdoo.FromString,
        )


class OdooServicer(object):
  """*
  List of available functions for Odoo only.
  Don't forget to authenticate yourself with metadata "authorization" with api_key
  """

  def UpdateEmployee(self, request, context):
    """/ Update employee
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEmployees(self, request, context):
    """/ Stream of employees
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddEmployee(self, request, context):
    """/ Add employee, get the id as return.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEmployeeHolidays(self, request, context):
    """/ Stream of holidays for 1 specific employee
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHolidays(self, request, context):
    """/ Stream of holidays for the company + employees that need to be synchronized with Odoo
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddHoliday(self, request, context):
    """/ Add holiday, get the id as return.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropHoliday(self, request, context):
    """/ Remove holiday from database
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateHoliday(self, request, context):
    """/ Update holiday. raise error if fails
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDepartments(self, request, context):
    """/ return a stream of departments
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddDepartment(self, request, context):
    """/ Add department, get the id as return.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateDepartment(self, request, context):
    """/ Update a department. raise error if fails
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNewAttendance(self, request, context):
    """/ return a stream of attendance record + odoo employee id that have not yet been synchronized with Odoo or that need to be synchronized again.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPositions(self, request, context):
    """rpc SyncAttendance (stream LogEventOdooSync) returns (Empty); /// Send a stream of LogEventSync to confirm the log entries have been synchronized with Odoo. This funciton use a stream in order to synchronize a large bunch of records very quickly. Odoo can not update or create or delete LogEvent record in Weladee.
    / return a stream of positions. Called "job title" in odoo
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPosition(self, request, context):
    """/ Add position, get the id as return.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProjects(self, request, context):
    """/ return stream of timesheet project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OdooServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateEmployee': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateEmployee,
          request_deserializer=odoo__pb2.EmployeeOdoo.FromString,
          response_serializer=weladee__pb2.Empty.SerializeToString,
      ),
      'GetEmployees': grpc.unary_stream_rpc_method_handler(
          servicer.GetEmployees,
          request_deserializer=odoo__pb2.OdooRequest.FromString,
          response_serializer=odoo__pb2.EmployeeOdoo.SerializeToString,
      ),
      'AddEmployee': grpc.unary_unary_rpc_method_handler(
          servicer.AddEmployee,
          request_deserializer=odoo__pb2.EmployeeOdoo.FromString,
          response_serializer=weladee__pb2.AddResult.SerializeToString,
      ),
      'GetEmployeeHolidays': grpc.unary_stream_rpc_method_handler(
          servicer.GetEmployeeHolidays,
          request_deserializer=odoo__pb2.OdooRequest.FromString,
          response_serializer=odoo__pb2.HolidayOdoo.SerializeToString,
      ),
      'GetHolidays': grpc.unary_stream_rpc_method_handler(
          servicer.GetHolidays,
          request_deserializer=weladee__pb2.Empty.FromString,
          response_serializer=odoo__pb2.HolidayOdoo.SerializeToString,
      ),
      'AddHoliday': grpc.unary_unary_rpc_method_handler(
          servicer.AddHoliday,
          request_deserializer=odoo__pb2.HolidayOdoo.FromString,
          response_serializer=weladee__pb2.AddResult.SerializeToString,
      ),
      'DropHoliday': grpc.unary_unary_rpc_method_handler(
          servicer.DropHoliday,
          request_deserializer=odoo__pb2.OdooRequest.FromString,
          response_serializer=weladee__pb2.Empty.SerializeToString,
      ),
      'UpdateHoliday': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateHoliday,
          request_deserializer=odoo__pb2.HolidayOdoo.FromString,
          response_serializer=weladee__pb2.Empty.SerializeToString,
      ),
      'GetDepartments': grpc.unary_stream_rpc_method_handler(
          servicer.GetDepartments,
          request_deserializer=odoo__pb2.OdooRequest.FromString,
          response_serializer=odoo__pb2.DepartmentOdoo.SerializeToString,
      ),
      'AddDepartment': grpc.unary_unary_rpc_method_handler(
          servicer.AddDepartment,
          request_deserializer=odoo__pb2.DepartmentOdoo.FromString,
          response_serializer=weladee__pb2.AddResult.SerializeToString,
      ),
      'UpdateDepartment': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateDepartment,
          request_deserializer=odoo__pb2.DepartmentOdoo.FromString,
          response_serializer=weladee__pb2.Empty.SerializeToString,
      ),
      'GetNewAttendance': grpc.unary_stream_rpc_method_handler(
          servicer.GetNewAttendance,
          request_deserializer=odoo__pb2.AttendanceRequest.FromString,
          response_serializer=odoo__pb2.LogEventOdoo.SerializeToString,
      ),
      'GetPositions': grpc.unary_stream_rpc_method_handler(
          servicer.GetPositions,
          request_deserializer=weladee__pb2.Empty.FromString,
          response_serializer=odoo__pb2.PositionOdoo.SerializeToString,
      ),
      'AddPosition': grpc.unary_unary_rpc_method_handler(
          servicer.AddPosition,
          request_deserializer=odoo__pb2.PositionOdoo.FromString,
          response_serializer=weladee__pb2.AddResult.SerializeToString,
      ),
      'GetProjects': grpc.unary_stream_rpc_method_handler(
          servicer.GetProjects,
          request_deserializer=weladee__pb2.Empty.FromString,
          response_serializer=odoo__pb2.ProjectOdoo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.weladee.com.Odoo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))