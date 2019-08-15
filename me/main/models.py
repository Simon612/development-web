from django.db import models

# Create your models here.
class Text(models.Model):
    text2 = models.TextField()

class MainText(models.Model):
    text = models.TextField()

class lists(models.Model):
    list = models.TextField()

class Emails(models.Model):
    Lists = models.ForeignKey(lists, on_delete=models.CASCADE)
    txt = models.CharField(max_length=400)





