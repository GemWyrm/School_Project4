from django.db import models

class Chart(models.Model):
    graph = models.ImageField(default='graph/img.png')
