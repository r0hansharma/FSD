"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from first_app import views
from my_app import views as my_app_views
from todo_api import urls as todo_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.profile, name='profile'),
    path('profile.html', views.profile, name='profile'),
    path('tic_tac_toe.html', views.tictactoe, name='tictactoe'),
    path('wordle.html', views.wordle, name='wordle'),
    path('blog.html', views.blog, name='blog'),
    path('employee.html', views.employee, name='employee'),

    path('index/', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('help.html', views.help, name='help'),
    #path('forms.html', views.forms, name='forms'),
    path('forms/', views.get_degree,  name='forms'),
    path('forms.html', views.get_degree,  name='forms'),
    path('students/', views.get_students,  name='students'),
    path('students.html', views.get_students,  name='students'),
    path('search.html', views.search,  name='search'),
    path('search/', views.search,  name='search'),
    

    path('signup/', my_app_views.UserSignup.as_view(), name='signup'),
    path('accounts/login/', my_app_views.UserLogin.as_view(), name='login'),
    path('logout/', my_app_views.UserLogin.as_view(), name='logout'),
    path('person-create/', my_app_views.PersonCreate.as_view(), name='personcreate'),
    path('', my_app_views.PersonList.as_view(), name='personlist'),
    path('person-detail/pk=<int:pk>', my_app_views.PersonDetail.as_view(), name='persondetail'),
    path('person-update/pk=<int:pk>', my_app_views.PersonUpdate.as_view(), name='personupdate'),
    path('person-delete/pk=<int:pk>', my_app_views.PersonDelete.as_view(), name='persondelete'),

    #path('', include('blog.urls')),
    #path('', include('first_app.urls')),
    #path('', include('my_app.urls')),
    #path('', include('todo_api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include(todo_urls)),
   
]
