from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserType(models.Model):
    type = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return str(self.type)

class Project(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, default="", blank= True)
    completed = models.BooleanField(default=False, blank= True)
    date_of_creation = models.DateField(auto_now_add=True, null=True, blank= True)
    date_of_start = models.DateField(auto_now_add=False, null=True, blank= True)
    date_of_end = models.DateField(auto_now_add=False, null=True, blank= True)
    responsible = models.ForeignKey(User, null=True, related_name='assignee1', on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, null=True, related_name='creator1', on_delete=models.DO_NOTHING)

    border_color = models.CharField(max_length=8, default="#ffffff")

    def __str__(self):
        return str(self.title)

class State(models.Model):
    title = models.CharField(max_length=255, null=True, blank= True)
    description = models.CharField(max_length=255, null=True, default="", blank= True)
    user_type = models.ForeignKey(UserType, null=True, on_delete=models.DO_NOTHING)
    order = models.IntegerField(null=False, blank= False)
    forward_movement_emp = models.BooleanField(default=True)
    backward_movement_emp = models.BooleanField(default=True)
    forward_movement_manager = models.BooleanField(default=True)
    backward_movement_manager = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

class status(models.Model):
    title = models.CharField(max_length=255, null=True, blank= True)
    description = models.CharField(max_length=255, null=True, default="", blank= True)
    user_type = models.ForeignKey(UserType, null=True, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

class Department(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null = True, blank =True)

    def __str__(self):
        return str(self.title)

class WorkPackage2(models.Model):
    title= models.CharField(max_length=255, null=False, blank= False)
    description = models.CharField(max_length=255, default="", blank= True)
    completed = models.BooleanField(default=False, blank= True)

    date_of_creation = models.DateField(auto_now_add=True, blank= True)

    planned_date_of_start = models.DateField(auto_now_add=False, null=True, blank= True)
    planned_date_of_end = models.DateField(auto_now_add=False, null=True, blank= True)

    duration = models.IntegerField(null=True, blank= True)

    actual_date_of_start = models.DateField(auto_now_add=False, null=True, blank= True)
    actual_date_of_end = models.DateField(auto_now_add=False, null=True, blank= True)

    efforts_actual = models.IntegerField(null=True)
    efforts_planned = models.IntegerField(null=True)

    responsible = models.ForeignKey(User, null=True, related_name='assignee4', on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, null=True, related_name='creator4', on_delete=models.DO_NOTHING)

    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    
    state = models.ForeignKey(State, null=True, on_delete=models.DO_NOTHING, default = 1)

    inputFrom = models.ForeignKey('self', null=True, related_name='input_from', on_delete=models.DO_NOTHING)
    inputFile = models.FileField(upload_to='documents/', blank=True)

    border_color = models.CharField(max_length=8, default="#f5f5f5")

    def __str__(self):
        return str(self.title)

    class Meta:
        order_with_respect_to = 'responsible'

class WorkPackage3(models.Model):
    
    title= models.CharField(max_length=255, null=False, blank= False)
    description = models.CharField(max_length=255, default="", blank= True)
    completed = models.BooleanField(default=False, blank= True)

    date_of_creation = models.DateField(auto_now_add=True, blank= True)

    planned_date_of_start = models.DateField(auto_now_add=False, null=True, blank= True)
    planned_date_of_end = models.DateField(auto_now_add=False, null=True, blank= True)

    duration = models.IntegerField(null=True, blank= True)

    actual_date_of_start = models.DateField(auto_now_add=False, null=True, blank= True)
    actual_date_of_end = models.DateField(auto_now_add=False, null=True, blank= True)

    efforts_actual = models.IntegerField(null=True)
    efforts_planned = models.IntegerField(null=True)

    responsible = models.ForeignKey(User, null=True, related_name='assignee5', on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, null=True, related_name='creator5', on_delete=models.DO_NOTHING)

    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    parentPackage = models.ForeignKey(WorkPackage2, null=True, on_delete=models.CASCADE)
    
    state = models.ForeignKey(State, null=True, on_delete=models.DO_NOTHING, default = 1)

    emp_status = models.ForeignKey(status, null=True, related_name='employee_status', on_delete=models.DO_NOTHING)
    manager_status = models.ForeignKey(status, null=True, related_name='manager_status', on_delete=models.DO_NOTHING, default = 4)

    inputFrom = models.ForeignKey('self', null=True, related_name='input_from', on_delete=models.DO_NOTHING)
    inputFile = models.FileField(upload_to='documents/', blank=True)

    border_color = models.CharField(max_length=8, default="#f5f5f5")

    def __str__(self):
        return str(self.title)

    class Meta:
        order_with_respect_to = 'responsible'


class UserProfileDetail(models.Model):
    
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null = True)
    phone = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length=200, null = True)
    profile_pic = models.ImageField(default="default_profile.png", null = True, blank = True)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType, null=True, on_delete=models.DO_NOTHING, default=1)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)

def create_profile(sender, instance, created, **kwargs):
    if created:
        new_user = UserProfileDetail.objects.create(user = instance, name = instance.first_name +" "+ instance.last_name)
               
        print("Profile Created!", instance.first_name)

post_save.connect(create_profile, sender = User)
