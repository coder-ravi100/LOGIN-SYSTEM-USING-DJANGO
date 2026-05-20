from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from .form import RegistrationForm

# Create your views here.
def dashboard(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    user = User.objects.get(id=user_id)

    # return render(request, 'dashboard.html', {
    #     'user': user,
    #     'role' : user.role
    # })
    messages.success(request, "Accounts Login Successfully..! Welcome Your Dashboard")
    context = {
        'user' : user,
        'role' : user.role,
    }
    return render(request, 'Dashboard.html',context)


def registration(request):
    
    form = RegistrationForm()

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = User(
                username = username,
                email = email,
                role = role
            )

            user.set_password(password)

            user.save()

            messages.success(request, "Accounts Created Successfully")

            return redirect('login')
        
    context = {
        'form' : form
    }

    return render(request, 'registration_page.html',context)


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email = email)
            if user.check_password(password):
                request.session['user_id'] = user.id
                request.session['role'] = user.role
                
                #Role Based Redirect
                if user.role =="admin":
                    return redirect('dashboard')
                
                elif user.role == "teacher":
                    return redirect('dashboard')
                
                elif user.role == "student":
                    return redirect('dashboard')
                
            else:
                # return render(request,'login_page.html',{
                #     'error' :'Wrong Password'
                # })
                messages.error(request, "Wrong Password")
                return redirect('login')
                
        except:
            # return render(request, 'login_page.html', {
            #     'error' :  'User Not Found'
            # })
            messages.error(request,"User Not Found")
            return redirect('login')
        
    
    return render(request, 'Login_page.html')

def logout(request):
    request.session.flush()
    messages.success(request, "Accounts Logout Successfully..!")
    return redirect('login')
