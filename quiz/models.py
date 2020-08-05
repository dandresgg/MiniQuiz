from django.db import models
import jsonfield

# Create your models here.
class Quiz(models.Model):
    data = jsonfield.JSONField(blank=True, null=True)