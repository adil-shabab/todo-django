from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title