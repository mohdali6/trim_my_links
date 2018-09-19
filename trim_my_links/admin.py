# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Link
# Register your models here.


class LinkAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Link._meta.get_fields()]

	fieldsets = [
		('New Generated Trimmed Link', {'fields': ['trimmed_link']}),
		('Original Big Link', {'fields': ['original_link']})
	]

admin.site.register(Link, LinkAdmin)