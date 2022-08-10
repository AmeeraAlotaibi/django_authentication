from django.db import OperationalError
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from movies import forms, models


def get_movies(request: HttpRequest) -> HttpResponse:
    try:
        movies: list[models.Movie] = list(models.Movie.objects.all())
    except OperationalError:
        movies = []

    context = {
        "movies": movies,
    }
    return render(request, "movie_list.html", context)


def get_movie(request: HttpRequest, movie_id: int) -> HttpResponse:
    try:
        movie: models.Movie = models.Movie.objects.get(id=movie_id)
    except (OperationalError, models.Movie.DoesNotExist):
        raise Http404(f"no movie found matching {movie_id}")

    context = {
        "movie": movie,
    }
    return render(request, "movie_detail.html", context)


@login_required
def create_movie(request: HttpRequest) -> HttpResponse:
    form = forms.MovieForm()
    if request.method == "POST":
        # BONUS: This needs to have the `user` injected in the constructor
        # somehow
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "create_movie.html", context)
