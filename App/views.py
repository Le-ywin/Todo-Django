from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic import View
from App.forms import *
from App.models import *
from App.models import TaskModel
from django.contrib.auth import *
import random
from django.core.mail import send_mail
from django.utils.decorators import method_decorator

# Create your views here.

# signup,login,Task,add,read,task delete,task update,logout,forgot password

def is_user(fn):

    def wrapper(request,*args,**kwargs):

        id = kwargs.get("id")

        item = TaskModel.objects.get(id=id)

        if item.user_id == request.user:

            return fn(request,**kwargs)
        
        return redirect("login")
    
    return wrapper


# Sign Up
# url : http://127.0.0.1:8000/todo/signup

class UserRegisterationView(View):

        def get(self,request):

            form = UserregistrationForm

            return render(request,"signup.html",{"form":form})
        
        def post(self,request):

            form = UserregistrationForm(request.POST)

            if form.is_valid():

                print(form.cleaned_data)

                username = form.cleaned_data.get('username')

                password = form.cleaned_data.get('password')

                email = form.cleaned_data.get('email')

                User.objects.create_user(username = username,password = password,email = email)

                form = UserregistrationForm()

                return redirect('login')

            return render(request,"signup.html",{"form":form})
            

# Login
# url : http://127.0.0.1:8000/login/

class LoginView(View):
     
     def get(self,request):
          
        form = LoginForm()
          
        return render(request,"login.html",{"form":form})
     
     def post(self,request):
          
        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")

            password = form.cleaned_data.get("password")

            login_obj = authenticate(request,username=username,password=password)

            if login_obj:

                login(request,login_obj)

                return redirect("taskview")
            
            else:

                return render(request,"login.html",{"form":form})
            
# Logout
# url : http://127.0.0.1:8000/logout/

class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect('login')

# Create
# url : http://127.0.0.1:8000/taskadd/

class TaskAddView(View):

    def get(self,request):

        form = TaskForm

        return render(request,"taskadd.html",{'form':form})
    
    def post(self,request):

        form = TaskForm(request.POST)

        if form.is_valid():

            TaskModel.objects.create(user_id = request.user,**form.cleaned_data)
            
        form = TaskForm()

        return render(request,"taskadd.html",{'form':form})

# Read
# url : http://127.0.0.1:8000/taskview/

class TaskReadView(View):

    def get(self,request):

        result = TaskModel.objects.all()

        return render(request,"taskview.html",{'result':result})

# Update
# url : http://127.0.0.1:8000/taskupdate/id

@method_decorator(decorator=is_user,name="dispatch")
class TaskUpdateView(View):

    def get(self,request,id):

        item = TaskModel.objects.get(id = id)

        form = TaskForm(instance=item)

        return render(request,"taskupdate.html",{'form':form})
    
    def post(self,request,**kwargs):

        id = kwargs.get('id')
        
        item = TaskModel.objects.get(id = id)

        form = TaskForm(request.POST,instance=item)

        if form.is_valid():

            form.save()
        
        form = TaskForm()
        
        return render(request, "taskupdate.html", {'form': form})

# Delete
# url : http://127.0.0.1:8000/deletetask/id
@method_decorator(decorator=is_user,name="dispatch")
class TaskDeleteView(View):

    def get(self,request,**kwargs):

        id = kwargs.get('id')

        item = TaskModel.objects.get(id=id)

        item.delete()

        return redirect('taskview')
    

# To read a specific task 
@method_decorator(decorator=is_user,name="dispatch")
class TaskDetailView(View):

    def get(self, request, **kwargs):

        id = kwargs.get('id')

        item = TaskModel.objects.get(id=id)

        return render(request, "taskdetail.html", {'item': item})
    

class ForgotPasswordView(View):

    def get(self,request):
    
        form = ForgotPasswordForm

        return render(request,"forgotpwd.html",{"form":form})
    
    def post(self,request):

        form = ForgotPasswordForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get("email")

            user = User.objects.get(email=email)

            otp = random.randint(1000,9999)

            OtpModel.objects.create(user_id = user, otp = otp)
            # qatt gfcf msgl gczv  >>  App Password
            # ramadasvtk@gmail.com >>  Official App mail ID
            send_mail(subject="OTP New Password",message=f"Your OTP for Password Rest is : {str(otp)}",from_email="ramadasvtk@gmail.com",recipient_list=[email])

            return redirect("verify")

        return render(request,"forgotpwd.html")
        
class OtpVeifyView(View):

    def get(self,request):

        form = OtpForm

        return render(request,"otpform.html",{"form":form})
    
    def post(self,request):

        form = OtpForm(request.POST)

        if form.is_valid():

            otp = form.cleaned_data.get("otp")

            result = OtpModel.objects.get(otp = otp)

            user_id = result.user_id

            user = User.objects.get(id = user_id.id)

            username = user.username

        if result:

            request.session['user'] = username

            return redirect("reset")

        return render(request,"pwdreset.html",{"form":form})
        
class PwdResetView(View):

    def get(self,request):

        form = PwdResetForm

        return render(request,"pwdreset.html",{"form":form})
    
    def post(self,request):

        form = PwdResetForm(request.POST)

        if form.is_valid():

            password = form.cleaned_data.get('password')

            confirm_password = form.cleaned_data.get('confirm_password')

            if password == confirm_password:

                username = request.session.get('user')

                user = User.objects.get(username = username)

                user.set_password("password")

                user.save()

                return redirect("login")
            
            return render(request,"pwdreset.html",{"form":form})
        

class TaskFilterView(View):

    def get(self,request):

        category = request.GET.get('category')

        Task = TaskModel.objects.filter(user_id = request.user)

        tasks = Task.filter(task_category = category)

        return render(request,"filter.html",{"tasks":tasks})
    

class IndexView(View):

    def get(self,request):

        return render(request,"index.html")


class TaskEdit(View):

    def get(self,request,**kwargs):

        id = kwargs.get("id")

        data = TaskModel.objects.get(id=id)

        data.completed_status = True

        data.save()

        return redirect("taskview")