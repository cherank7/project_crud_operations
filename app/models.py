from django.db import models

# Create your models here.
class TOPIC(models.Model):
    topic_name=models.CharField(max_length=100)
    def __str__(self):
        return self.topic_name


class WEB(models.Model):
    topic_name=models.ForeignKey(TOPIC,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    dob=models.DateField()
    email=models.EmailField()
    def __str__(self):
        return self.name


class ACCESS(models.Model):
    name=models.ForeignKey(WEB,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    url=models.URLField()

