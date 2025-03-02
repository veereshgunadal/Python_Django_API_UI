from django.shortcuts import render,redirect

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
        # data_obj is single model object and to iterate in loop made as list element
        data_obj = [data_obj,]
        return render(request, 'getmovie_result.html', {'movies':data_obj} )
    except Exception as e:
        print(e)
        return redirect("not_found")
    
def add_movie(request):
    form = MoviesForm
    context = {}
    context['form'] = form
    return render(request, "addmovie.html", context)

def add_movie_result(request):
    if request.method == "POST":
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'addupdatedeletemovie_result.html', {'action':'add movie'})
        else:
            return redirect("allmovie_result")
        
def update_movie(request):
    return render(request, 'updatemovie.html')

def updating_movie(request, **kwargs):
    if kwargs == {}:
        name = request.GET.get("name")
    else:
        name = kwargs['name']
    print(name)
    try:
        data_obj = Movies.objects.get(name = name)
        name = data_obj.name
        form = MoviesForm
        return render(request, 'updatingmovie.html', {'form':form, 'moviename':name})
    except Exception as e:
        print(e)
        return redirect("not_found")

def update_movie_result(request, name):
    data_obj = Movies.objects.get(name = name)
    if request.method == "POST":
        form = MoviesForm(request.POST, instance = data_obj)
        if form.is_valid():
            form.save(commit = True)
            return render(request, 'addupdatedeletemovie_result.html', {'action': 'update'})
        else:
            print(form.errors)
            return redirect("not_found")
        
def delete_movie(request):
    return render(request, 'deletemovie.html')

def delete_movie_result(request, **kwargs):
    if kwargs == {}:
        name = request.GET.get("name")
    else:
        name = kwargs['name']
    try:
        data_obj = Movies.objects.get(name = name)
        status, data = data_obj.delete()
        if status == 1:
            return render(request, 'addupdatedeletemovie_result.html', {'action': 'delete'})
        else:
            return redirect("not_found")
    except Exception as e:
        print(e)
        return redirect("not_found")

def all_movie_result(request):
    try:
        data_obj = Movies.objects.all()
        # data_obj is query set and already its list of movies object
        return render(request, 'getmovie_result.html', {'movies': data_obj} )
    except Exception as e:
        print(e)
        return redirect("not_found")

def not_found(request):
    return render(request, "notfound.html")