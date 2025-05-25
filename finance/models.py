from django.db import models
from django.contrib.auth.models import User


class Doxod(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
    
class Rasxod(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
