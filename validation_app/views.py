from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages


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
    
    if request.method == "POST":
    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        user = User(username = username, 
                    email = email, 
                    role = role
                    )
        #USERNAME VALIDATION
        if len(username) > 50:
            messages.error(request, "Username Must Be At Least 3 Characters")
            return redirect("registration")
    
        #EMAIL VALIDATION
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email Already Exists")
            return redirect("registration")
        
        #PASSWORD VALIDATION
        if len(password) < 6:
            messages.error(request, "Password Must Be At Least 6 Characters")
            return redirect("registration")
        
        #Strong Password Validation
        if password.isdigit():
            messages.error(request, "Password Cannot Be Only Numbers")
            return redirect("registration")
        
        if not username.isalnum():
            messages.error(request, "Username Must Contain Only Letters And Numbers")
            return  redirect('registration')
        
        
        user.set_password(password)
        user.save()

        messages.success(request, "Accounts Successfully..!")

        return redirect('login')
    return render(request, 'registration_page.html')



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
