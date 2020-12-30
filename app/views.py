from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, Http404, get_object_or_404

def index(request):

    
    posts = Post.objects.all()
    

    if request.method == "POST":
        
       
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.text = form.cleaned_data["text"]
            post.image = form.cleaned_data["image"]
            post.user =request.user
            post.save()

            return redirect('index')
    else:
        form = PostForm()

            
    return render(request, "app/index.html", {   
        'form':form,
        'posts':posts,

    })

def profile_view(request):
    
    posts = Post.objects.filter(user=request.user)
      
    try:
        p = Profile.objects.get(user=request.user)
        
    except :
        p = None
    if request.method == "POST":
       
        bio =  BioForm()
       
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
           
            profile, created = Profile.objects.get_or_create(user=request.user)
            
            profile.image = form.cleaned_data["image"]
            profile.user =request.user
            profile.save()

            return redirect('profile')
    else:
        form = ProfileForm()
        bio =  BioForm()
    return render(request, "app/profile.html", {     
        'form':form,
        'posts':posts,
        'bio':bio,
        'profile':p,
        
    })

def editBio(request):
    if request.method == "POST":
        
        
        form = BioForm(request.POST)
        
        if form.is_valid():
            profile, created = Profile.objects.get_or_create(user=request.user)
            print(profile)
            profile.bio = request.POST["bio"]
            profile.user =request.user
            profile.save()

            return redirect('profile')
