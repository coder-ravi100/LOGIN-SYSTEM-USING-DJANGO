from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def dashboard(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    user = User.objects.get(id=user_id)

    return render(request, 'dashboard.html', {
        'user': user,
        'role' : user.role
    })


def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        role = request.POST['role']

        user = User(username = username, email = email, role = role)

        user.set_password(password)
        user.save()

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
                return render(request,'login_page.html',{
                    'error' :'Wrong Password'
                })
        except:
            return render(request, 'login_page.html', {
                'error' :  'User Not Found'
            })
        
    return render(request, 'Login_page.html')

def logout(request):
    request.session.flush()
    return redirect('/login/')