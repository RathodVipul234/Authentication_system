from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import signup,login
from .form import signupForm,loginForm
# Create your views here.
def home(request):
    return render(request,'index.html')
def Signup(request):
    #bellow code for if you want to submit data from html file (*without creating form)
    data = signup()
    if request.method == 'POST':
        data.Name = request.POST['name']
        data.Email = request.POST['email']
        data.Password = request.POST['password']
        signup.save(data)
        
    # now using form
    
    # data = signupForm()
    # if request.method == 'POST':
    #     data = signupForm(request.POST)
    #     if data.is_valid():
    #         data.save()
    return render(request,'Signup.html')
     

def Signin(request):
    # No need to use form
    # form = loginForm()
    data1 = login()
    if request.method == "POST":
        try:
            Email = request.POST['email']
            Password = request.POST['password']
            obj = signup.objects.get(Email=Email)
            if obj.Password == Password:
                data1.Email = Email
                data1.Password = Password
                login.save(data1)
                return redirect('/')

            else:
                return HttpResponse("Wrong Password")
        except:
            return HttpResponse("No user found")
    return render(request,'Signin.html')