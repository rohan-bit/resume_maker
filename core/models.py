from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=150)
    phone_no = PhoneNumberField(null=False,blank=False)

# to create the user because it extenstion of user model
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# to save the user profile 
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Project(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    project_name = models.CharField(max_length = 150)
    project_bio = models.TextField()
    project_tech_stack = models.CharField(max_length=255)
    project_team_size = models.IntegerField(validators=[MinValueValidator(1)])
    project_start_date = models.DateTimeField()
    project_github_link = models.CharField(max_length = 150)

class Education(models.Model):
    STATUS = (
        ('10th', ('10th')),
        ('12th', ('12th')),
        ('undergraduate', ('undergraduate')),
        ('graduate',('graduate')),
    )
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length = 150,choices = STATUS,default=1)
    percentage = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100)])
    school_name = models.CharField(max_length = 100,null=True)
    present = models.BooleanField(default=False,null=False)
    start_year=models.SmallIntegerField(blank=True, null=True)
    grad_year = models.SmallIntegerField(blank=True, null=True)

class work_exp(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=150,null=False,default='')
    company_location = models.CharField(max_length=150,null=False,default='')
    job_position = models.CharField(max_length = 150)
    present = models.BooleanField(default=False,null=False)
    end_date = models.DateTimeField(default=datetime.now(),null=True)
    start_date = models.DateTimeField()
    job_description = models.TextField()

class skillset(models.Model):
    STATUS = (
        ('Advanced', ('Advanced')),
        ('Intermidate', ('Intermidate')),
        ('Beginner', ('Beginner')),
    )
    profile = models.ManyToManyField(Profile,null=True)
    skill_name = models.CharField(max_length=30)
    level = models.CharField(max_length=32,choices=STATUS,
      default=3)

class position_of_reponsiblity(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    position = models.CharField(max_length=255,null=False)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

class Awards(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    des = models.TextField()

class messages(models.Model):
    sender_profile = models.ForeignKey(Profile,on_delete = models.CASCADE,null=True,related_name='sender_profile')
    is_anon = models.BooleanField(null=False,default=False)
    receiver_profile = models.ForeignKey(Profile,on_delete = models.CASCADE,null=True,related_name='reciver_profile')
    note = models.TextField(null=True)

# class Resume(models.Model):
#     profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
#     projects = models.ManyToManyField(Project,null=True)
#     skills = models.ManyToManyField(skillset,null=True)
#     work_exp_resume = models.ManyToManyField(work_exp,null=True)
