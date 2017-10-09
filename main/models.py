# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=180)
    author=models.CharField(max_length=30)

    def __str__(self):
    	return self.title