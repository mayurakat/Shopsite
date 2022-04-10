from django.shortcuts import render,redirect
from shop.models import product
from django.contrib import messages
from django.contrib.auth.models import  User, auth
from django.urls import reverse
# Create your views here.
def home(request):
    top_two = product.objects.all()[:2]
    return render(request,"home.html",{'tops':top_two})

def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username = username).exists():
                messages.info(request, "username taken")
                return redirect('register')
                
            elif User.objects.filter(email = email).exists():
                messages.info(request,"email taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username = username, email= email, password = password1, first_name = first_name , last_name = last_name )
                user.save();
                print("user Created")
                messages.info(request, "user Create")
                return redirect('login')
        else:
            messages.info(request,"password not match")
            return redirect('register')

    else:
        return render(request, 'register.html')
def login(request):


    if request.method == 'POST':


        username = request.POST.get('username')
        password = request.POST.get('password')
        

        

        user = auth.authenticate(username=username,password=password)

        if user:

                auth.login(request,user)
                return redirect('home')
        else:

                messages.info(request,'invalid user and password')
                return redirect('login')
       
    else:

        return render(request,"login.html")


def logout(request):
    if request.session:
        messages.success(request,'succesfully logout')
    else:
        messages.error(request,'session expired login again')
    auth.logout(request)
    return redirect(reverse('home'))