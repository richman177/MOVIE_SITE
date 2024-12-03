from .models import Movie, Country, Director, Actor, Genre
from modeltranslation.translator import TranslationOptions,register

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name', 'director_biography')



@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'actor_biography')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)
