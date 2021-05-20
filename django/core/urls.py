from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    path('movies/<int:movie_id>/image/upload/', views.MovieImageUpload.as_view(), name='MovieImageUpload'),
    path('movies/<int:movie_id>/vote/<int:pk>/', views.UpdateVote.as_view(), name='UpdateVote'),
    path('movies/<int:movie_id>/vote/', views.CreateVote.as_view(), name='CreateVote'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='MovieDetail'),
    path('movies/top/', views.TopMovies.as_view(), name='TopMovies'),
    path('movies/', views.MovieList.as_view(), name='MovieList'),

]
