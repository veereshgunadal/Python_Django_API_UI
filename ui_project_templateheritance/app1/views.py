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
        context = {}
        context['movie'] = data_obj
        return render(request, 'getmovie_result', context )
    except:
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
            return render(request, 'addmovie_result.html')
    
def not_found(request):
    return render(request, "notfound.html")