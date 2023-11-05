from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import movies
from .models import userinputs
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserInputForm
from django.db.models.signals import pre_save,post_save
from django.http import JsonResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(request):
    blog=movies.objects.all()
    return render(request,'review/home.html',{'blog':blog})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'review/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'review/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'review/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'review/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'review/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

# @login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else :
        return redirect('home')


# -------------------------------
def all_blogs(request,key):
    blogs=movies.objects.all()
    # key =request.GET.get('key','chetan')
    u=userinputs.objects.all()
    movie = get_object_or_404(movies, m_name=key)
    r=movie.rating
    rating_range=range(1,r+1)
    return render(request,'review/blog.html',{'blogs':blogs,'key':key,'u':u,'rating_range':rating_range})

def genre(request,key):
    blogs=movies.objects.all()
    return render(request,'review/genre.html',{'blogs':blogs,'key':key})





def comments(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            cby=request.user.username
            con= request.POST['con']
            ron=request.POST['star']
            
            c= request.POST['c']
            if len(c)>100:
                messages.error(request, "Commments must be under 100 charcters!!")
            elif len(c)<1:
                messages.error(request, "Comments can'tmovie_name be empty!!")
            else:
                userinputs(m_name=con,u_name=cby,review=c,rating=ron).save()
                messages.success(request, "your comments saved successfully !")
    else:
        messages.error(request, "You must be logged in for rating!!")
    blogs=movies.objects.all()
        # key =request.GET.get('key','chetan')
    u=userinputs.objects.all()
    key=request.POST['con']
    movie = get_object_or_404(movies, m_name=key)
    r=movie.rating
    rating_range=range(1,r+1)
    
    return render(request,'review/blog.html',{'blogs':blogs,'key':key,'u':u,'rating_range':rating_range})
    
    
    
from django.shortcuts import render
from .models import movies  # Import your model

def search_view(request):
    query = request.GET.get('q')  # Get the search query from the form

    if query:
        # Use the query to search your movies model and retrieve relevant results
        results = movies.objects.filter(m_name__icontains=query).union(
            movies.objects.filter(genre__icontains=query)).union(movies.objects.filter(release_year__icontains=query))  # Modify this to fit your search criteria

        context = {
            'results': results,
            'query': query,
        }
        return render(request, 'review/search_results.html', context)

    return redirect(reverse('home'))    # Handle the case where no results are found

from django.shortcuts import render
from .models import movies

def sortby(request,key):
    
    if key == 'rating':
        movies_list = movies.objects.order_by('-rating')
    elif key == 'az':
        movies_list = movies.objects.order_by('m_name')
    elif key == 'za':
        movies_list = movies.objects.order_by('-m_name')
    elif key == 'old':
        movies_list = movies.objects.order_by('release_year')
    elif key == 'new':
        movies_list = movies.objects.order_by('-release_year')
    context = {
        'movies_list': movies_list,
        'sort_by': key,  # Pass the selected sorting option to the template
    }
    return render(request, 'review/sortby.html', context)