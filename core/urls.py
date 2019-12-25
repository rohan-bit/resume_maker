from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sign_up',views.signup,name='signup'),
    path('add_project',views.add_project,name='add_project'),
    path('view_project',views.view_project,name='view_project'),
    path('logout',views.logout_user,name='logout'),

    # path(),
]