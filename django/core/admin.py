from django.contrib import admin

from .models import Movie, Vote, MovieImage


admin.site.register(Vote)
admin.site.register(Movie)
admin.site.register(MovieImage)