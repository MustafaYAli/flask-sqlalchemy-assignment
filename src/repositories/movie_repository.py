# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from sqlalchemy import Column, Integer, String  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from models import Movie


class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        Movies = Movie.query.all()
        return Movies
    

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        Movie = Movie.query.filter_by(id=movie_id).first()
        return Movie

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        movie = Movie(title=title, director=director, rating=rating)
        return movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        Movies = Movie.query.filter(Movie.title.like(f'%{title}%')).all()
        return Movies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
