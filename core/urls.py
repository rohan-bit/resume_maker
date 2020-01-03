from django.urls import path, re_path
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
    path('work_exp',views.view_work_exp,name='view_work_exp'),
    path('add_skills',views.add_skillset,name='add_skills'),
    path('view_skills',views.view_skillset,name='view_skills'),
    path('add_position_of_responsibilty',views.add_por,name='add_position_of_responsibilty'),
    path('view_position',views.view_por,name='view_position'),
    path('resume_choice',views.resume_choice),
    re_path(r'^resume/(?P<value>\d+)/$',views.resume_maker),
    re_path(r'^portfolio/(?P<username>[\w.@+-]+)/$',views.portfolio),
    path('login',auth_views.LoginView.as_view(template_name="/home/rohan/resume_maker/core/templates/login.html"),name='login'),
    path('logout',views.logout_user,name='logout'),
    # path(),
]