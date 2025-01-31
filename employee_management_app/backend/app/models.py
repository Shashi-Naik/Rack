from django.db import models

class Rack(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    columns = models.IntegerField()

class Slot(models.Model):
    rack = models.ForeignKey(Rack, related_name='slots', on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()
    name = models.CharField(max_length=255, default="Slot")
