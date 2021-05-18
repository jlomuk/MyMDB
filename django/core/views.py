from django.shortcuts import render
from django.views import generic 

from .models import Movie, Person


class MovieList(generic.ListView):
    model = Movie
    paginate_by = 5


class MovieDetail(generic.DetailView):
    queryset = Movie.objects.all_with_related_persons()


class PersonDetail(generic.DetailView):
    queryset = Person.objects.all_with_prefetch_movies()

