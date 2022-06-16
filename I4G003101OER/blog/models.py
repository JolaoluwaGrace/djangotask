from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField()
    Authors = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()