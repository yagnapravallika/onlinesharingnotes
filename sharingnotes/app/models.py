from django.db import models
class Teacher(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    classno=models.IntegerField()
class Student(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=30)
    classno=models.IntegerField()
class Fileupload(models.Model):
    name=models.CharField(max_length=30)
    classno=models.IntegerField()
    file=models.FileField(upload_to='file/')



