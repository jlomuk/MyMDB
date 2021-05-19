from django.contrib import admin

from .models import Movie, Vote


admin.site.register(Vote)
admin.site.register(Movie)