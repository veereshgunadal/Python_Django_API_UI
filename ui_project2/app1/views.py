from django.shortcuts import render, redirect

from app1.models import Movies
from app1.forms import MoviesForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def get_movie(request):
    return render(request, 'getmovie.html')

def get_movie_result(request):
    try:
        name = request.GET.get("name")
        data_obj = Movies.objects.get(name = name)
        res_data = {'name': data_obj.name, 'release_date': data_obj.release_date, 'actor': data_obj.actor,
                    'actress': data_obj.actress, 'language': data_obj.language, 'rating': data_obj.rating}
        return render(request, 'getmovie_result.html', res_data)
    except Exception as e:
        print(e)
        return redirect("not_found")
    
def not_found(request):
    return render(request, 'not_found.html')

def add_movie(request):
    form = MoviesForm
    context = {}
    context['form'] = form
    return render(request, 'addmovie.html', context)

def add_movie_result(request):
    try:
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'addmovie_result.html')
        else:
            return redirect("not_found")
    except Exception as e:
        print(e)
        return redirect("not_found")

def update_movie(request):
    return render(request, 'updatemovie.html')

def updating_movie(request):
    try:
        name = request.GET.get("name")
        data_obj = Movies.objects.get(name = name)
        form = MoviesForm
        context = {}
        context['form'] = form
        return render(request, 'updatingmovie.html', context)
    except Exception as e:
        print(e)
        return redirect("not_found")
    
def update_movie_result(request):
    name = request.POST.get("name")
    data_obj = Movies.objects.get(name = name)
    if request.method == "POST":
        form = MoviesForm(request.POST, instance=data_obj)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'updatemovie_result.html')
        print(form.errors)
        return redirect("not_found")

def delete_movie(request):
    return render(request, 'deletemovie.html')

def delete_movie_result(request):
    try:
        name = request.GET.get("name")
        data_obj = Movies.objects.get(name = name)
        status, data = data_obj.delete()
        if status == 1:
            return render(request, 'deletemovie_result.html')
    except:
        return redirect("not_found")