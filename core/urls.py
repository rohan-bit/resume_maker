from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('sign_up',views.signup,name='signup'),
    path('add_project',views.add_project,name='add_project'),
    path('view_project',views.view_project,name='view_project'),
    path('login',auth_views.LoginView.as_view(template_name="/home/rohan/resume_maker/core/templates/login.html"),name='login'),
    path('logout',views.logout_user,name='logout'),

    # path(),
]