from django.contrib import admin
from formapi.models import users

class users(models.Model):
    uid = models.CharField(max_length=50, null=False)
    datatest = models.CharField(max_length=50, null=False)
    
 def __str__(self):
    return self.uid
