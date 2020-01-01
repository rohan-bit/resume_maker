from django.contrib.auth.forms import UserCreationForm
from django import forms
from core.models import Profile,Project,Education,work_exp,skillset,position_of_reponsiblity
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class SignUpForm(UserCreationForm):
    phone_no = PhoneNumberField()
    address = forms.CharField(max_length=150)
    class Meta :
        model = User
        fields = ('username','email','first_name','last_name','password1','password2','address','phone_no',)

class Add_Project(forms.ModelForm):
    class Meta :
        model = Project
        fields = ('project_name','project_bio','project_tech_stack','project_team_size','project_start_date','project_github_link',)

class Add_Edu(forms.ModelForm):
    class Meta :
        model = Education
        fields = ('title','percentage','grad_year',)

class Add_Work_Exp(forms.ModelForm):
    class Meta :
        model = work_exp
        fields = ('job_position','start_date','job_description')

class Add_SkillSet(forms.ModelForm):
    class Meta :
        model = skillset
        fields = ('skill_name','level',)


class Add_postion_of_responsibilty(forms.ModelForm):
    class Meta :
        model = position_of_reponsiblity
        fields = ('position','start_date','end_date')



# def add_project():
#     pass
#
# def delete_project():
#     pass
#
# def update_project():
#     pass
#
# def