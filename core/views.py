from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from core.forms import SignUpForm,Add_Project
from core.models import Profile,Project
# Create your views here.
def index(request):
    return  render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() :
            user = form.save()
            user.refresh_from_db()# to activate the signal of profile model
            user.profile.address = form.cleaned_data.get('address')
            user.profile.phone_no = form.cleaned_data.get('phone_no')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request,user)
            return redirect('index')
    else :
        form = SignUpForm()
    return render(request,'signup.html',{'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

@login_required
def add_project(request):
    # print('rohan')
    if request.method == 'POST' :
        form = Add_Project(request.POST)
        if form.is_valid():
            project = form.save()
            project.profile = request.user.profile
            project.save()
            return redirect('index')
    else :
        form = Add_Project()
    return render(request,'add_project.html',{'form':form})

@login_required
def add_edu(request):
    pass


@login_required
def work_exp(request):
    pass


@login_required
def pos(request):
    pass

@login_required
def view_project(request):
    pro = request.user.profile
    project=Project.objects.filter(profile=pro)
    #print(project)
    return render(request,'view_project.html',{'project':project})
# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.address = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()
