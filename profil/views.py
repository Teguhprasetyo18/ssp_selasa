from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def cerita(request):
    return render(request,'cerita.html')

def berita(request):
    return render(request,'berita.html')