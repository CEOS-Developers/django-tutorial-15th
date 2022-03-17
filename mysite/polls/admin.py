from django.contrib import admin

from .models import Question

admin.site.resister(Question)