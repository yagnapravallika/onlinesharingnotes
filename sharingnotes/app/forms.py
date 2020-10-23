from .models import Teacher,Student,Fileupload
from django import forms
class Teacherform(forms.ModelForm):
    class Meta:
        model=Teacher
        fields="__all__"
        labels={
            'idno':'IDNO',
            'name':'NAME',
            'password':'PASSWORD',
            'subject':'SUBJECT',
            'classno':'CLASS'

        }
class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        labels={
            'idno':'IDNO',
            'name':'NAME',
            'password':'PASSWORD',
            'classno':'CLASS'
        }
class Fileuploadeform(forms.ModelForm):
    class Meta:
        model=Fileupload
        fields="__all__"
        labels={
            'classno':'CLASS',
            'file':'FILE'
        }