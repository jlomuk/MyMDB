from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic 
from django.urls import reverse

from .models import Movie, Person, Vote
from .forms import VoteForm


class MovieList(generic.ListView):
    model = Movie
    paginate_by = 5


class CreateVote(LoginRequiredMixin, generic.CreateView):
    form_class = VoteForm

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        initial['movie'] = self.kwargs['movie_id']
        return initial

    def get_success_url(self):
        movie_id = self.object.movie.id
        return reverse('core:MovieDetail', kwargs= {'pk': movie_id})

    def render_to_response(self, context, **response_kwargs):
        print(context)
        movie_id = context['object'].id
        movie_detail_url = reverse('core:MovieDetail', kwargs={'pk': movie_id})
        return redirect(to=movie_detail_url)


class UpdateVote(LoginRequiredMixin, generic.UpdateView):
    form_class = VoteForm
    queryset = Vote.objects.all()

    def get_object(self, queryset=None):
        vote = super().get_object(queryset)
        user = self.request.user
        if vote.user != user:
            raise PermissionDenied('cannot change another user vote')
        return vote

    def get_success_url(self):
        movie_id = self.object.movie.id
        return reverse('core:MovieDetail', kwargs= {'pk': movie_id})

    def render_to_response(self, context, **response_kwargs):
        movie_id = context['object'].id
        movie_detail_url = reverse('core:MovieDetail', kwargs={'pk': movie_id})
        return redirect(to=movie_detail_url)



class MovieDetail(generic.DetailView):
    queryset = Movie.objects.all_with_related_persons_and_score()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(
                movie=self.object, user=self.request.user)
            if vote.id:
                vote_form_url = reverse('core:UpdateVote', 
                            kwargs={
                                'movie_id':vote.movie.id,
                                'pk': vote.id,
                            })
            else:
                vote_form_url = reverse('core:CreateVote',
                            kwargs={
                                'movie_id': self.object.id
                            })
            vote_form = VoteForm(instance=vote)
            ctx['vote_form'] = vote_form
            ctx['vote_form_url'] = vote_form_url
        return ctx

class PersonDetail(generic.DetailView):
    queryset = Person.objects.all_with_prefetch_movies()

