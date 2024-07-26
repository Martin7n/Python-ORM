import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Count, Avg, F, Q

from main_app.models import Director, Actor, Movie


# Create queries within functions


# director = Director.objects.all().annotate(movie_count=Count('movies_director')).order_by('-movie_count', 'full_name')



#
# def get_directors(search_name=None, search_nationality=None):
#     directors = None
#     if search_name is None and search_nationality is None:
#         return ''
#     if search_name is not None and search_nationality is not None:
#         directors = Director.objects.filter(full_name__icontains=search_name, nationality__icontains=search_nationality).order_by('full_name')
#     elif search_name is not None:
#         directors = Director.objects.filter(full_name__icontains=search_name).order_by('full_name')
#
#     elif search_nationality is not None:
#         director = Director.objects.filter(nationality__icontains=search_nationality).order_by('full_name')
#
#     if not directors:
#         return ""
#     return '/n'.join(f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}" for director in directors)





def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ''

    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = Q(query_name & query_nationality)
    elif search_name is not None:
        query = query_name
    elif search_nationality is not None:
        query = query_nationality

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""
    return '\n'.join(f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}" for director in directors)
    # result = []
    # for d in directors:
    #     result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")
    #
    # return '\n'.join(result)




def get_top_director():

    top_director = Director.objects.annotate(movies_count=Count('movies_director')).order_by('-movies_count','full_name').first()
    if top_director is None or not Movie.objects.all():
        return ""
    return f"Top Director: {top_director.full_name}, movies: {top_director.movies_count}."

# print(get_top_director())



def get_top_actor():
    top_actor = Actor.objects.annotate(movies_count=Count('movies_staring_actors'), average_rating=Avg('movies_staring_actors__rating')).order_by('-movies_count','full_name').first()
    if not Movie.objects.all() or not top_actor:
        return ""
    movies = Movie.objects.filter(starring_actor=top_actor)
    actor_movies = ', '.join(x.title for x in movies)
    if actor_movies is None:
        return ""
    avg_rating = top_actor.average_rating
    if avg_rating is None:
        return ""
    return f"Top Actor: {top_actor.full_name}, starring in movies: {actor_movies}, movies average rating: {avg_rating:.1f}"

# print(get_top_actor())

def get_actors_by_movies_count():
    actors = Actor.objects.annotate(movies_count=Count('movies_actor')).order_by('-movies_count', 'full_name')[:3]

    if not actors or not Movie.objects.all():
        return ''
    # if not actors or not actors[0].movies_count:
    #     return ''
    return "\n".join([f'{actor.full_name}, participated in {actor.movies_count} movies' for actor in actors])

# print(get_actors_by_movies_count())
#
# def get_top_rated_awarded_movie():
#     awarded_movies = Movie.objects.filter(is_awarded=True).annotate(avg_rating=Avg('rating')).order_by('-avg_rating', 'title').first()
#     if not awarded_movies or not Movie.objects.all():
#         return ""
#
#     title = awarded_movies.title
#     rating = awarded_movies.rating
#     staring_actor = awarded_movies.starring_actor.full_name if awarded_movies.starring_actor.full_name else 'N/A'
#     cast = ', '.join([cast.full_name for cast in awarded_movies.actors.order_by("full_name")])
#     # print(title, rating, staring_actor, cast)
#
#     return f"Top rated awarded movie: {title}, rating: {rating:.1f}. Starring actor: {staring_actor}. Cast: {cast}."



def get_top_rated_awarded_movie():
    top_movie = Movie.objects\
        .select_related('starring_actor')\
        .prefetch_related('actors')\
        .filter(is_awarded=True)\
        .order_by('-rating', 'title')\
        .first()

    if top_movie is None:
        return ''

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else 'N/A'

    participating_actors = top_movie.actors.order_by('full_name').values_list('full_name', flat=True)

    cast = ', '.join(participating_actors)

    return f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating:.1f}."\
            f" Starring actor: {starring_actor}. Cast: {cast}."


print(get_top_rated_awarded_movie())
def increase_rating():
    movies = Movie.objects.filter(is_classic=True, rating__lt=10)
    if not movies:
        return "No ratings increased."

    updated_movies =  movies.update(rating=F('rating')+0.1)

    return f'Rating increased for {updated_movies} movies.'

print(increase_rating())

