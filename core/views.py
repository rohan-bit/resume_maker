from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from core.forms import SignUpForm,Add_Project,Add_Edu,Add_Work_Exp,Add_SkillSet
from core.models import Profile,Project,Education,work_exp,skillset
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

#adding the elemenet
@login_required
def add_project(request):
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
    if request.method == 'POST' :
        form = Add_Edu(request.POST)
        if form.is_valid() :
            education = form.save()
            education.profile = request.user.profile
            education.save()
            return redirect('index')
    else :
        form = Add_Edu()
    return render(request,'add_edu.html',{'form':form})




@login_required
def add_work_exp(request):
    if request.method == 'POST' :
        form = Add_Work_Exp(request.POST)
        if form.is_valid():
            work_exp = form.save()
            work_exp.profile = request.user.profile
            work_exp.save()
            return  redirect('index')
    else :
        form = Add_Work_Exp()
    return render(request,'add_work_exp.html',{'form':form})

@login_required
def add_skillset(request):
    if request.method == 'POST' :
         form = Add_SkillSet(request.POST)
         if form.is_valid():
             skills = form.save()
             skills.profile.add(request.user.profile)
             skills.save()
             return redirect('index')
    else :
        form = Add_SkillSet()
    return render(request,'add_skillset.html',{'form':form})

@login_required
def view_work_exp(request):
    pass

@login_required
def pos(request):
    pass


#viewing
@login_required
def view_project(request):
    pro = request.user.profile
    project=Project.objects.filter(profile=pro)
    return render(request,'view_project.html',{'project':project})

@login_required
def view_education(request):
    profile = request.user.profile
    edu = Education.objects.filter(profile=profile)
    return render(request,'view_education.html',{'edu':edu})

@login_required
def view_skillset(request):
    profile = request.user.profile
    skills = skillset.objects.filter(profile=profile)
    return render(request,'view_skill.html',{'skills':skills})
# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.address = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()
