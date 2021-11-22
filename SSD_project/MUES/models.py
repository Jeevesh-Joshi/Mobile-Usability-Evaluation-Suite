from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    tasks = models.ManyToManyField('Tasks')

    def __str__(self):
        return self.name

class Tasks(models.Model):
    project = models.ForeignKey(Projects,on_delete=CASCADE,related_name="pp")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Users(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]
    name = models.CharField(max_length=20)
    project = models.ForeignKey(Projects,on_delete=CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=6,choices=GENDER,default='male')
    tasks = models.ManyToManyField(Tasks)
    problems = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Videos(models.Model):
    user = models.ForeignKey(Users,on_delete=CASCADE)
    task = models.ForeignKey(Tasks,on_delete=CASCADE)
    path = models.CharField(max_length=500)

    def __str__(self):
        return self.user.name