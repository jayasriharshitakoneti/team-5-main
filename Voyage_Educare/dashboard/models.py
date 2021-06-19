from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class NGO(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=1000)
    trainer_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class SchoolLeader(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=1000)
    school_name = models.CharField(max_length=70)
    leader_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name  = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=1000)
    teacher_id = models.AutoField(primary_key=True)
    points = models.FloatField()
    badge = models.CharField(max_length=50)
    rank = models.IntegerField()

    def __str__(self):
        return self.name


