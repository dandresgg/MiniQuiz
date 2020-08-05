from django.db import models
import jsonfield

# Create your models here.
data = jsonfield.JSONField(blank=True, null=True)