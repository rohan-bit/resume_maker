from django.http import HttpResponse,FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from core.forms import SignUpForm,Add_Project,Add_Edu,Add_Work_Exp,Add_SkillSet,Add_postion_of_responsibilty,message_form,sharing_form
from core.models import Profile,Project,Education,work_exp,skillset,position_of_reponsiblity,User,messages
from django.template.loader import get_template
import tempfile
import subprocess
from django.core.mail import send_mail
from django.conf import settings
from subprocess import Popen, PIPE
import os
import pdflatex
import sys
from datetime import datetime


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
            work_exp.end_date = form.cleaned_data.get('end_date')
            #print(work_exp.end_date)
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
def add_por(request):
    if request.method == 'POST':
        form = Add_postion_of_responsibilty(request.POST)
        if form.is_valid():
            por = form.save()
            por.profile=request.user.profile
            #por.profile.add(request.user.profile)
            por.save()
            return redirect('index')
    else :
        form = Add_postion_of_responsibilty()
    return render(request,'add_por.html',{'form':form})



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
def view_work_exp(request):
    profile = request.user.profile
    works = work_exp.objects.filter(profile=profile)
    return render(request,'view_work_exp.html',{'works':works})


@login_required
def view_skillset(request):
    profile = request.user.profile
    skills = skillset.objects.filter(profile=profile)
    return render(request,'view_skill.html',{'skills':skills})


@login_required
def view_por(request):
    profile = request.user.profile
    pors = position_of_reponsiblity.objects.filter(profile=profile)
    return render(request,'view_por.html',{'pors':pors})


@login_required
def resume_maker(request,value):
    user1 = request.user
    profile = request.user.profile
    skills = skillset.objects.filter(profile=profile).order_by('level')
    projects = Project.objects.filter(profile=profile).order_by('-project_start_date')
    edu = Education.objects.filter(profile=profile).order_by('-grad_year')
    work = work_exp.objects.filter(profile=profile).order_by('-start_date')
    pors = position_of_reponsiblity.objects.filter(profile=profile).order_by('-start_date')
    context = {'user': user1, 'profile': profile, 'projects': projects, 'edu': edu, 'work': work, 'skills': skills,
               'pors': pors}
    resume_final = 'resume'+value+'.tex'
    template = get_template(resume_final)
    rendered_resume = template.render(context).encode('UTF-8')
    file_name = user1.first_name+'_'+user1.last_name+'_'+value+'.tex'
    file_name_pdf = user1.first_name+'_'+user1.last_name+'_'+value+'.pdf'
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        completeName = os.path.join(tmpdirname, file_name)
        completeName_pdf = os.path.join(tmpdirname,file_name_pdf)
        f = open(completeName, "wb+")
        f.write(rendered_resume)
        f.close()
        proc = subprocess.Popen(['pdflatex', '-output-directory',tmpdirname, completeName])
        proc.communicate()
        return FileResponse(open(completeName_pdf, "rb"), content_type='application/pdf')
    return redirect('index')


@login_required
def resume_choice(request):
    return render(request,'resume_to_pdf.html')


#porfolio site
def portfolio(request,username):
    user1 = User.objects.get(username=username)
    profile = user1.profile
    user_outsider = request.user
    skills = skillset.objects.filter(profile=profile).order_by('level')
    projects = Project.objects.filter(profile=profile).order_by('-project_start_date')
    edu = Education.objects.filter(profile=profile).order_by('-grad_year')
    work = work_exp.objects.filter(profile=profile).order_by('-start_date')
    pors = position_of_reponsiblity.objects.filter(profile=profile).order_by('-start_date')
    context = {'user':user1,'profile':profile,'projects':projects,'edu':edu,'works':work,'skills':skills,'pors':pors,'user_outsider':user_outsider}
    return render(request,'portfolio.html',context)


@login_required
def send_message(request,username):
    if request.method == 'POST' :
        form = message_form(request.POST)
        if form.is_valid():
            mess = form.save()
            mess.sender_profile = request.user.profile
            user1 = User.objects.get(username=username)
            mess.receiver_profile = user1.profile
            mess.time_of_message = datetime.now()
            mess.save()
            return redirect('index')
    else :
        form = message_form()
    return render(request,'send_message.html',{'form':form})


@login_required
def view_message(request):
    messages_obj = messages.objects.filter(receiver_profile=request.user.profile).order_by('-time_of_message')
    return render(request,'view_message.html',{'messages':messages_obj})


@login_required
def share(request):
    if request.method == 'POST':
        form = sharing_form(request.POST)
        if form.is_valid():
            subject = 'Check out the profile of '+request.user.first_name+' '+request.user.last_name
            message = 'Hi there,'+'\n'+'Check out the profile of '+request.user.first_name+' '+request.user.last_name+' on our website.\n'+' Warm Regards,\n'+'Rohan Talwar'
            email_from = settings.EMAIL_HOST_USER
            print(form.cleaned_data.get('email_id'))
            recipient_list = [form.cleaned_data.get('email_id'),]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('index')
    else :
        form = sharing_form()
    return render(request,'sharing.html',{'form':form})

# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.address = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()

