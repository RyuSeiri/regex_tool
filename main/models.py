from django.db import models

class Regex(models.Model):
    pattern = models.CharField(max_length=100)
    text = models.TextField()
    result = models.TextField()
