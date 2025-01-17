# Weladee - Odoo

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/weladee)


![Weladee logo](https://vgy.me/jlVton.png)![odoo](https://vgy.me/5KoRp0.png)

## What is Weladee?

Weladee is a service "In The Cloud" to manage employee attendance.
It's developed to be **simple**, **fast** and **cheap** to use for any small company (or even big ones).
The primary market of this service is **Thailand** for now (2018), we started to deploy customers in Cambodia too.

Take a look at https://www.weladee.com

### Why using Weladee?

Because employee lateness and absenteeism cost a lot of money to your company.
Weladee provides a very easy way to reduce it.

See how much lateness costs you with our simulation page: https://www.weladee.com/simulation

## Description

[Odoo](https://www.odoo.co.th) module for Weladee

This Odoo module create the link between Weladee and your Odoo 14.0 instance.

You will be able to synchronize departments, employees and attendance. Import expenses, timesheet, leave, holidays, ... from Weladee to your Odoo instance.

## What is synschronized

### Bi-Directional between Odoo-Weladee / Weladee-Odoo

The idea is to use Weladee a HRMS addon to Odoo. So mostof the data is collected in Weladee and then imported to Odoo.

There are 3 exceptions:

- Department
- Employee
- Position

These 3 data can be sent to Weladee from Odoo and vice versa.

In case of conflict, the most recent data will be used.
It shouldn't be a problem because the data is not often updated. The HR operator should decice which app to use to update the data. Create employee on Weladee is probably the best move.


![](https://www.plantuml.com/plantuml/svg/SoWkIImgAStDuGfFpKbCIKrLiD6rK_1FoS-tKWZ8ByuioSpFmoBbabe0r9QRcbU2HT8rjo0dlp8rbOlB8JKl1MWs0000)


### Uni-Directional from Weladee to Odoo

This data is sent from Weladee to Odoo. Weladee feeds Odoo with HRMS data.

- Attendance
- Leave
- Timesheet (project, task)
- Job classifieds (https://job.weladee.com)
- Expenses

![](http://www.plantuml.com/plantuml/svg/SoWkIImgAStDuGfFpKbCIKrLqBLJy4_9pxTIS2mfISrBISnBJiMKyqbDBCCY79APcrgSaPfQWYdbbP-4AUXQKP2QLvnQpEK0j0de2000)




## Technical


### Install modules


![](https://i.imgur.com/4g13hYX.png)

### gRPC

[gRPC](https://grpc.io) is used to communicate with [weladee](https://www.weladee.com) server.
The http2 protocol and stream push between client and server offer excellent performances.
The communication between Odoo & Weladee is encrypted with SSL3 and TLS 1.3 certificate.

Sample calls:

![uml](https://goo.gl/AFpwfs)

### API Key

To connect your Odoo instance to [weladee](https://www.weladee.com) server you need an api key.
The api key is available when you create an account at https://www.weladee.com/register

Weladee is free to subscribe with 3 months trial period or even 100% free for company with less than 5 employees.

## Sample Code for gRPC API

It's ready for Odoo 14. gRPC code is compatible python 3.

### Connect to server

```python
    import grpc
    import . from weladee_pb2
    import . from weladee_pb2_grpc
  

    # Weladee grpc server address is grpc.weladee.com:22443
    address = "grpc.weladee.com:22443"

    # Define a secure channel with embedded public certificate

    creds = grpc.ssl_channel_credentials(certificate)
    channel = grpc.secure_channel(address, creds)
```

### Provide api-key and get some data

This code retrieve the list of departments and add a holiday to Weladee.

```python
    # Connect from Odoo
    # Place here the token specific to each company. It's called api_key in table company

    authorization = [("authorization", "bc7f3c00-bfa4-4ac2-810b-a11dca5ec48e")]

    stub = weladee_pb2_grpc.OdooStub(channel)

    # List all departments
    print("Departments")
    for dept in stub.GetDepartments(myrequest, metadata=authorization):
        print(dept)

    # Add new holiday
    newHoliday = weladee_pb2.HolidayOdoo()
    newHoliday.Holiday.date = 20170918
    newHoliday.Holiday.name_english = "Company holiday"
    newHoliday.odoo.odoo_id = 9
    try:
        result = stub.AddHoliday(newHoliday, metadata=authorization)

        print (result.id)
    except Exception as e:
        print("Add holiday failed",e)
```

### Get all logs from Weladee not yet sync with Odoo

Simple code parsing a stream of log events that need to be synchronized with Odoo.

```python
    # List of attendance to sync
    print("Attendance to sync")
    i=0
    for att in stub.GetNewAttendance(weladee_pb2.Empty(), metadata=authorization):
        i+=1
        logging.log(i,att)
```

### Deleted records


If records have been deleted on Weladee, you will call gRPC function **GetDeleted**. It will return all IDs of deleted record for a specific table.


![](https://img.shields.io/badge/Developed%20by%20-Frontware%20International-orange)
--------------------------------------------------------------
(c) 2022 [Frontware International Co,Ltd.](https://www.frontware.co.th)
