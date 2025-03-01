from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from django.core.serializers import serialize

from app1.models import Student
from app1.forms import StudentForm

import json

# Create your views here.

class Students(View):
    def get(self, request, *args, **kwargs):
         rollno = kwargs.get('rollno', 0)
         try:
             if rollno == 0:
                 data_obj = Student.objects.all()
             else:
                 data_obj = []
                 data_obj.append(Student.objects.get(roll_no = rollno))
             for i in data_obj:
                 retrieved_data = {'name': i.name, 'roll_no': i.roll_no, 'age': i.age,
                                   'addr': i.addr, 'ph_no': i.ph_no, 'department': i.department}
             res_data = json.dumps(retrieved_data)
             return HttpResponse(res_data, content_type = 'application/json', status = 200)	
         except Exception as e:
             print(e)
             res_data = json.dumps({'errorcode': 404, 'errormessage':'resource not found'})
             return HttpResponse(res_data, content_type = 'application/json', status = 404)

    def get(self, request, *args, **kwargs):
        rollno = kwargs.get('rollno', 0)
        try:
            if rollno == 0:
                data_obj = Student.objects.all()
            else:
                data_obj = []
                data_obj.append(Student.objects.get(roll_no = rollno))
            res_data = serialize('json', data_obj)
            return HttpResponse(res_data, content_type = 'application/json', status = 200)
        except Exception as e:
            print(e)
            res_data = json.dumps({'errorcode': 404, 'errormessage':'resource not found'})
            return HttpResponse(res_data, content_type = 'application/json', status = 404)

    def post(self, request, *args, **kwargs):
        req = request.body
        print(req)
        print(type(req))
        try:
            req_data = json.loads(req)
            form = StudentForm(req_data)
            if form.is_valid():
                form.save(commit = True)
                res_data = json.dumps({'code':201, 'message':'resource created'})
                return HttpResponse(res_data, content_type = 'application/json', status = 201)
            if form.errors:
                res = {'errorcode':400, 'errormessage':'fields validation failed'}
                res.update(form.errors)
                res_data = json.dumps(res)
                return HttpResponse(res_data, content_type = 'application/json', status = 400)
        except ValueError:
            res_data = json.dumps({'errorcode':400, 'errormessage':'payload is not valid json'})
            return HttpResponse(res_data, content_type = 'application/json', status = 400)

    def put(self, request, rollno, *args, **kwargs):
        req = request.body
        try:
            req_data = json.loads(req)
            
            data_obj = Student.objects.get(roll_no = rollno)
            retrieved_data = {'name': data_obj.name, 'roll_no': data_obj.roll_no, 'age': data_obj.age,
                             'addr': data_obj.addr, 'ph_no': data_obj.ph_no, 'department': data_obj.department}
            retrieved_data.update(req_data)
            form = StudentForm(retrieved_data, instance=data_obj)
            if form.is_valid():
                form.save(commit = True)
                res_data = json.dumps({'code':200, 'message':'resource updated'})
                return HttpResponse(res_data, content_type = 'application/json', status = 200)
            if form.errors:
                res = {'errorcode':400, 'message':'fields validation failed'}
                res.update(form.errors)
                res_data = json.dumps(res)
                return HttpResponse(res_data, content_type = 'application/json', status = 400)
        except ValueError:
            res_data = json.dumps({'errorcode':400, 'errormessage':'payload is not valid json'})
            return HttpResponse(res_data, content_type = 'application/json', status = 400)
        except:
            res_data = json.dumps({'errorcode':404, 'errormessage':'resource not found'})
            return HttpResponse(res_data, content_type = 'application/json', status = 404)

    def delete(self, request, rollno, *args, **kwargs):
        try:
            data_obj = Student.objects.get(roll_no = rollno)
            status, delete_data = data_obj.delete()
            res_data = json.dumps({'code':204, 'message':'resource deleted'})
            return HttpResponse(res_data, content_type = 'application/json', status =204)
            if status == 1:
                res_data = json.dumps({'code':204, 'message':'resource deleted'})
                return HttpResponse(res_data, content_type = 'application/json', status =204)
            else:
                res_data = json.dumps({'code':400, 'message':'unable to delete'})
                return HttpResponse(res_data, content_type = 'application/json', status = 400)
        except Exception as e:
            print(e)
            res_data = json.dumps({'errorcode':404, 'errormessage':'resource not found'})
            return HttpResponse(res_data, content_type = 'application/json', status = 404)
                    






















