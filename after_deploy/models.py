from django.db import models

class tasks(models.Model):
    code = models.CharField(max_length=32, primary_key=True, null=False, blank=False)
