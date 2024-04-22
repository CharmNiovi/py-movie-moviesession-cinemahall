from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()
    queryset = queryset.filter(
        genres__id__in=genres_ids
    ) if genres_ids else queryset
    queryset = queryset.filter(
        actors__id__in=actors_ids
    ) if actors_ids else queryset
    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet[Movie]:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)
