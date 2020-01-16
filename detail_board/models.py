from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Family_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
    scrap=models.ManyToManyField(User, blank=True,related_name="user_scrap")
class Traffic_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Government_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Army_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Labor_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Financial_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Trade_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Leisure_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Lawsuit_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Welfare_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Estate_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Business_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Crime_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Client_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Children_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Information_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Startup_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)
class Eco_Board(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100, null=True)
    answer = models.TextField()
    relevant_area=models.CharField(max_length=100,null=True)
    relevant_rule=models.CharField(max_length=100,null=True)