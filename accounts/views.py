from django.shortcuts import render,redirect
# Create your views here.
def dashboard(request):
    return render(request,'Dashboard_page.html')


def registration(request):
    pass

def login(request):
    pass

def logout(request):
    pass