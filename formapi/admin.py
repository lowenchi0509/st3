from django.contrib import admin
from formapi.models import users

class usersAdmin(admin.ModelAdmin):
    uid = models.CharField(max_length=50, null=False)
    datatest = models.CharField(max_length=50, null=False)
    
def __str__(self):
   return self.uid
admin.site.register(users,usersAdmin)

