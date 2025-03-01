from django.shortcuts import render

from django.views.generic import View
from django.http import HttpResponse
import json

from app1.models import Movies
from app1.forms import MoviesForm

# Create your views here.

# Website home page view
def home(request):
    return render(request, 'home.html')

# to get movie details
def get_movie(request):
    return render(request, 'getmovie.html')

# fetched get movie details 
def get_movie_result(request):
    try:
        name = request.GET.get("name")
        data_obj = Movies.objects.get(name = name)
        res_data = {'code': 200, 'message': 'resource found', 'name': data_obj.name, 'release_date': data_obj.release_date, 'actor': data_obj.actor,
                    'actress': data_obj.actress, 'language': data_obj.language, 'rating': data_obj.rating}
        return render(request, 'getmovie_result.html', res_data)
    except:
        res_data = {'code': 404, 'message': 'resource not found'}
        return render(request, 'getmovie_result.html', res_data)

# asking movie details in html form to add in database
def add_movie(request):
    moviesform = MoviesForm

    context = {}
    context['form'] = moviesform
    return render(request, 'addmovie.html', context)

# taking form inputs and adding movies to database and showing response
def add_movie_result(request):
    print(request.POST.get("name"))
    print(request.POST.get("release_date"))
    try:
        req_data = {'name': request.POST.get("name"), 'release_date': request.POST.get("release_date"), 'actor': request.POST.get("actor"),
                'actress': request.POST.get("actress"), 'language': request.POST.get("language"), 'rating': request.POST.get("rating")}

        form = MoviesForm(req_data)
        if form.is_valid():
            form.save(commit=True)
            res_data = {'code': 201, 'message':'movie added to list'}
            return render(request, 'addmovie_result.html', res_data)
        if form.errors:
            print(form.errors)
            res_data = {'code': 400, 'message':'payload error'}
            return render(request, 'addmovie_result.html', res_data)
    except:    
        res_data = {'code': 400, 'message':'payload error'}
        return render(request, 'addmovie_result.html', res_data)

# asking movie name to update
def update_movie(request):
    return render(request, 'updatemovie.html')

# inprogress (not completed)
def update_movie_result(request):
    form = MoviesForm
    context = {}
    context['form'] = form
    try:
        name = request.POST.get("name")
        data_obj = Movies.objects.get("name")
        return render(request, 'updatemovie_result.html',context)
    except:
        res_data = {'code': 400, 'message': 'payload error'}
        return render(request, 'updatemovie_result.html', res_data)


def delete_movie(request):
    return render(request, 'deletemovie.html')

def delete_movie_result(request):
    try:
        name = request.GET.get("name")
        data_obj = Movies.objects.get(name = name)
        print(data_obj)
        status, data = data_obj.delete()
        if status == 1:

            res_data = {'code': 204, 'message': 'deleted movie'}
            return render(request, 'deletemovie_result.html', res_data)
    except Exception as e:
        print(e)
        res_data = {'code': 404, 'message': 'resource not found'}
        return render(request, 'deletemovie_result.html', res_data)