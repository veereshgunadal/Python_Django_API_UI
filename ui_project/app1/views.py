from django.shortcuts import render
from app1.models import Student
from app1.forms import StudentForm

from django.core.serializers import serialize
from django.http import HttpResponse

import json

# Create your views here.

def home_page(request):
    return render(request, 'home_updated.html')

def post(request):
    context ={}
    context['form']= StudentForm()
    
    return render(request, 'post.html', context)

def patch(request):
    context ={}
    context['form']= StudentForm()
    return render(request, 'patch.html', context)

def get(request):
    return render(request, 'get.html')

def delete(request):
    return render(request, 'delete.html')

def get_result(request):
    req_data = request.GET.get('roll_no')
    data_obj = []
    data_obj.append(Student.objects.get(roll_no = req_data))
    res_data = serialize('json',data_obj)
    return HttpResponse(res_data, content_type='application/json')

def post_result(request):
    req_data = {'name':request.POST.get('name'), 'roll_no': request.POST.get('roll_no'), 'age': request.POST.get('age'),
                'addr':request.POST.get('addr'), 'ph_no': request.POST.get('ph_no'), 'department': request.POST.get('department')}

    print(req_data)
    form = StudentForm(req_data)
    if form.is_valid():
        form.save(commit=True)
        res_data = {'code':201, 'message':'created'}
        return render(request, 'results.html', res_data)
    if form.errors:
        form_error = json.loads(json.dumps(form.errors))
        form_error = list(form_error.values())
        res_data = {'code':400, 'message':form_error[0]}
        return render(request, 'results.html', res_data)

def patch_result(request):
    roll_no = request.POST.get('roll_no')
   
    try:
        data_obj = Student.objects.get(roll_no = roll_no)
        retrieved_data = {'name':data_obj.name, 'roll_no':data_obj.roll_no, 'age':data_obj.age,
                      'addr':data_obj.addr, 'ph_no':data_obj.ph_no, 'department':data_obj.department}

        req_data = {'name':request.POST.get('name'), 'age': request.POST.get('age'),
                    'addr':request.POST.get('addr'), 'ph_no': request.POST.get('ph_no'), 'department': request.POST.get('department')}

        retrieved_data.update(req_data)
        form = StudentForm(retrieved_data, instance = data_obj)
        if form.is_valid():
            form.save(commit=True)
            res_data = {'code':200, 'message':'created'}
            return render(request, 'results.html', res_data)
    except:
        res_data = {'code':400, 'message':'roll_no not exist'}
        return render(request, 'results.html', res_data)

def delete_result(request):
    req_data = request.GET.get('roll_no')
    data_obj = Student.objects.get(roll_no = req_data)
    status, data = data_obj.delete()
    if status == 1:
        return HttpResponse(json.dumps({'code':204}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'code':400}), content_type='application/json')