from django.shortcuts import render,redirect

from app1.models import Movies
from app1.forms import MoviesForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def add(request):
    form = MoviesForm
    return render(request, 'add.html', {'form':form})

def add_result(request):
    form = MoviesForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return render (request, 'addupdatedelete_result.html', {'action':'add movie'})
    else:
        return redirect("not_found")
    
def get(request):
    return render(request, 'get.html')

def get_result(request):
    try:
        name = request.GET.get("name")
        data_obj = Movies.objects.get(name = name)
        res_data = [data_obj,]
        return render(request, 'getresult.html', {'movies': res_data})
    except Exception as e:
        print(e)
        return redirect("not_found")

def all(request):
    try:
        data_obj = Movies.objects.all()
        return render(request, 'getresult.html', {'movies': data_obj})
    except Exception as e:
        print(e)
        return redirect("not_found")
    
def delete(request):
    return render(request, 'delete.html')

def delete_result(request):
    try:
        name = request.GET.get("name")
        data_obj = Movies.objects.get("name")
        status, data = data_obj.delete()
        if status == 1:
            return render(request, 'addupdatedelete_result.html', {'action': 'delete'})
    except:
        return redirect("not_found")
    
def update(request):
    return render(request, 'update.html')

def updating(request):
    try:
        form = MoviesForm
        name = request.GET.get("name")
        data_obj = Movies.objects.get(name = name)
        return render(request, 'updating.html', {'form': form, 'moviename':data_obj.name})
    except Exception as e:
        print(e)
        return redirect("not_found")
    
def update_result(request, name):
    try:
        data_obj = Movies.objects.get(name = name)
        form = MoviesForm(request.POST, instance= data_obj)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'addupdatedelete_result.html', {'action': 'update'})
        else:
            print(form.errors)
    except:
        return redirect("not_found")
    
def not_found(request):
    return render(request, 'notfound.html')