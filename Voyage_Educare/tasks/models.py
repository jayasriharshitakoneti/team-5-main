from django.db import models
from dashboard.models import Teacher
from dashboard.models import SchoolLeader
from dashboard.models import NGO
class Tasks(models.Model):
    task_id=models.AutoField(primary_key=True)
    task_title=models.CharField(max_length=50)
    task_desc=models.CharField(max_length=500)
    start_date=models.DateTimeField()
    deadline=models.DateTimeField()
    MaxPoints=models.IntegerField()
    attachments_url=models.URLField(max_length=100)

class Status(models.Model):
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE,)
    month = models.CharField(max_length=50)
    task_id=models.ForeignKey(Tasks)
    points=models.FloatField()
    isCompleted=models.BooleanField()


class FeedBack(models.Model):
    by_role=models.CharField(max_length=50)
    if(by_role=="Teacher"):
        by_id=models.ForeignKey(Teacher,on_delete=models.CASCADE,)
    elif(by_role=="School Leader"):
        by_id=models.ForeignKey(SchoolLeader,on_delete=models.CASCADE,)
    else:
        by_id=models.ForeignKey(NGO)
    desc=models.CharField(max_length=500)
    






