# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Link(models.Model):
	trimmed_link = models.CharField(max_length=8, unique=True)
	original_link = models.TextField(unique=True)
	timestamp = models.DateTimeField('date trimmed', auto_now_add=True)

	def __str__(self):
		return self.trimmed_link
