from django.db import models
from django.conf import settings
from django.db.models.aggregates import Sum


class MovieManager(models.Manager):
    
    def all_with_related_persons(self):
        qs = self.get_queryset()
        qs = qs.select_related('director')
        qs = qs.prefetch_related('writers', 'actors')
        return qs

    def all_with_related_persons_and_score(self):
        qs = self.all_with_related_persons()
        qs = qs.annotate(score=Sum('vote__value'))
        return qs

class Movie(models.Model):

    objects = MovieManager()

    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2 
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - NOT Rated'),
        (RATED_G, 'G - General Audiences'),
        (RATED_PG, 'PG - Parental Guidance Suggested'),
        (RATED_R, 'R - Restricted'),

    )

    title = models.CharField(max_length=140, verbose_name='Название')
    plot = models.TextField(verbose_name='Описание')
    year = models.PositiveIntegerField(verbose_name='Дата')
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED, verbose_name='Рейтинг')
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)
    director = models.ForeignKey(
        'Person', 
        on_delete=models.SET_NULL,
        related_name='directed',
        null=True,
        blank=True,
    )
    writers = models.ManyToManyField('Person', related_name='writing_credits', blank=True) 
    actors = models.ManyToManyField('Person', through='Role', related_name='acting_credits', blank=True) 

    def __str__(self):
        return f'{self.title} ({self.year})'

    class Meta:
        ordering = ('-year', 'title')
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class PersonManager(models.Manager):

    def all_with_prefetch_movies(self):
        qs = self.get_queryset()
        return qs.prefetch_related('directed', 'writing_credits', 'role_set__movie')


class Person(models.Model):

    first_name = models.CharField(max_length=140, verbose_name='Имя')
    last_name = models.CharField(max_length=140, verbose_name='Фамилия')
    born = models.DateField()
    died = models.DateField(null=True, blank=True)

    objects = PersonManager()

    class Meta:
        ordering = ('last_name', 'first_name',)

    def __str__(self):
        if self.died:
            return f'{self.last_name}, {self.first_name} ({self.born} - {self.dead})'
        return f'{self.last_name}, {self.first_name} ({self.born})'


class Role(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=140)

    def __str__(self):
        return f'{self.movie_id}, {self.person_id}, {self.name}'

    class Meta:
        unique_together = ('movie', 'person', 'name',)


class VoteManager(models.Manager):

    def get_vote_or_unsaved_blank_vote(self, movie, user):
        try:
            return Vote.objects.get(movie=movie, user=user)
        except Vote.DoesNotExist:
            return Vote(movie=movie, user=user)


class Vote(models.Model):
    UP = 1
    DOWN = -1
    VALUE_CHOICES = (
        (UP, '\U0001f44d'),
        (DOWN, '\U0001f44e'),
    )

    value = models.SmallIntegerField(choices=VALUE_CHOICES,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,)
    voted_on = models.DateTimeField(auto_now=True)

    objects = VoteManager()

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'