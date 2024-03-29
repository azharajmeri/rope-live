from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from api.models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class ProjectTableForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'onkeypress':'return enterKeyPress(event)'})
        }

class UserProfileDetailForm(forms.ModelForm):
    class Meta:
        model = UserProfileDetail
        fields = '__all__'
        exclude = ['user', 'date_created', 'date_created']


        widgets = {
            'profile_pic': forms.FileInput(attrs={'name':'profile_pic','class': 'form-control-file','placeholder':'Profile Photo...','id':'id_profile_pic', 'style':'width:85%!important'}),
        }

class PositionForm(forms.Form):
    position = forms.CharField()

class WorkPackageDetailsForm(forms.ModelForm):
    class Meta:
        model = WorkPackage3
        fields = ['title', 'description', 'emp_status', 'efforts_planned']

    def __init__(self, *args, **kwargs):
        super(WorkPackageDetailsForm, self).__init__(*args, **kwargs)
        self.fields['emp_status'].queryset = status.objects.filter(user_type=1, state = 2)
    
class WorkPackageCreationForm(forms.ModelForm):
    class Meta:
        model = WorkPackage3
        fields = ['title', 'parentPackage', 'inputFrom']

class Workpackage3DocumentForm(forms.ModelForm):
    class Meta:
        model = WorkPackage3
        fields = ['inputFile']
