from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def dashboard(request):
    return render(request,'Dashboard_page.html')

def signup(request):
    return render(request,'Login_page.html')

def signin(request):
    return render(request,'Registration_page.html')

def signout(request):
    return 