from django.shortcuts import render

# Create your views here.
def home(request):
    d = {"hobbies":['cricket','football']}
    return render(request, 'home.html',context=d)
def index(request):
    return render(request, 'index.html')