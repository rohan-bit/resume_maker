from django.contrib.auth.forms import UserCreationForm
from django import forms
from core.models import Profile,Project
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class SignUpForm(UserCreationForm):
    phone_no = PhoneNumberField()
    address = forms.CharField(max_length=150)
    class Meta :
        model = User
        fields = ('username','email','password1','password2','address','phone_no',)

class Add_Project(forms.ModelForm):
    class Meta :
        model = Project
        fields = ('project_name','project_bio','project_tech_stack','project_team_size','project_start_date','project_github_link',)


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