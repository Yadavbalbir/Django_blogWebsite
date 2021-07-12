from django.db.models import query
from django.http import request
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home/home.html')
    # return HttpResponse("Hello blog home")
def contact(request):
    messages.warning(request, 'Alert! Fill Your Details carefully!')
    if request.method=='POST':
        name=request.POST['name'],
        email=request.POST['email'],
        phone=request.POST['phone'],
        feedback=request.POST['feedback'],
        print(name,email,phone,feedback)     
        contact=Contact(name=name,email=email,phone=phone,feedback=feedback)
        contact.save()
        messages.success(request,"Thanks for giving feedback! Your feedback has been sent to admin.")
    return render(request,'home/contact.html')
    # return HttpResponse("Hello contact me here")
def about(request):
    return render(request,'home/about.html')
    # return HttpResponse("this is about section")

def search(request):
    # allposts=Post.objects.all()
    query=request.GET['query']
    allpostc = Post.objects.filter(content__icontains=query)
    allpostt=Post.objects.filter(title__icontains=query)
    allposts=allpostc.union(allpostt)
    params={'allposts':allposts}
    return render(request,'home/search.html',params )
    # return HttpResponse('We are seaching things')



def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']


        if len(username)>15 or len(username)<6:
            messages.error(request,'Username should be in between 6 to 15 characters')
            return redirect('home')

        if username.isalnum()==False:
            messages.error(request,'Username should be alpha numeric')
            return redirect('home')

        if len(email)<10:
            messages.error(request,'Please fill correct email address')
            return redirect('home')
        if len(password1)<8 or len(password2)<8:
               messages.error(request,'minimum length of password should be 8')
               return redirect('home')
        
        if password1 != password2:
               messages.error(request,'password and confirm password must be same')
               return redirect('home')



        myuser=User.objects.create_user(username,email,password1)
        myuser.first_name=fname
        myuser.last_name=lname 
        myuser.save()
        messages.success(request,"Congratulations! account created successfully")
        return redirect('home')
        
    else:
        return HttpResponse('404 Not Found')

def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invail username or passward")
            return redirect('home')
    else:
        return HttpResponse('login')
def handlelogout(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect('home')
