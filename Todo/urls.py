"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views as av

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',av.LoginView.as_view()),
    path('todo/signup',av.UserRegisterationView.as_view(),name="signup"),
    path('login/',av.LoginView.as_view(),name="login"),
    path('logout/',av.LogoutView.as_view(),name="logout"),
    path('taskadd/',av.TaskAddView.as_view(),name="add"),
    path('taskview/',av.TaskReadView.as_view(),name="taskview"),
    path('taskupdate/<int:id>',av.TaskUpdateView.as_view(),name="update"),
    path('deletetask/<int:id>',av.TaskDeleteView.as_view(),name="delete"),
    path('taskdetail/<int:id>',av.TaskDetailView.as_view(),name="detail"),
    path('forgot/',av.ForgotPasswordView.as_view(),name="forgot"),
    path('otpverify',av.OtpVeifyView.as_view(),name="verify"),
    path('todo/reset',av.PwdResetView.as_view(),name="reset"),
    path('filter/',av.TaskFilterView.as_view(),name="filter"),
    path('eidt/<int:id>',av.TaskEdit.as_view(),name="edit"),
    path('index/',av.IndexView.as_view(),name="index")
    
]