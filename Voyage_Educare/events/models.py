from django.db import models

# Create your models here.
class Events(models.Model):
    school_id=models.IntegerField()
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    #image_url=
    event_id=models.AutoField(primary_key=True)
    description=models.TextField()
    event_title=models.CharField(max_length=20)
    links=models.URLField()

    def __str__(self):
        return self.event_title