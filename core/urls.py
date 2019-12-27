from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('sign_up',views.signup,name='signup'),
    path('add_project',views.add_project,name='add_project'),
    path('view_project',views.view_project,name='view_project'),
    path('add_edu',views.add_edu,name='add_edu'),
    path('view_edu',views.view_education,name='view_edu'),
    path('add_work_exp',views.add_work_exp,name='add_work_exp'),
    path('add_skills',views.add_skillset,name='add_skills'),
    path('view_skills',views.view_skillset,name='view_skills'),
    path('login',auth_views.LoginView.as_view(template_name="/home/rohan/resume_maker/core/templates/login.html"),name='login'),
    path('logout',views.logout_user,name='logout'),

    # path(),
]