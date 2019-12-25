from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    project_team_size = models.IntegerField()
    project_start_date = models.DateTimeField()
    project_github_link = models.CharField(max_length = 150)

class Education(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length = 150)
    percentage = models.FloatField()
    grad_year = models.SmallIntegerField(blank=True, null=True)

class work_exp(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    job_position = models.CharField(max_length = 150)
    start_date = models.DateTimeField()
    job_des = models.TextField()

class position_of_reponsiblity(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    positon = models.CharField(max_length=255,null=False,default='0')

class Awards(models.Model):
    des = models.TextField()
