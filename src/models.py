# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from sqlalchemy import Column, Integer, String  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore

db = SQLAlchemy()  # type: ignore

class Movie(db.Model):
    __tablename__ = 'movies'
    movie_id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    rating = Column(Integer)

    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __repr__(self):
        return f'Movie({self.title}, {self.director}, {self.rating})'
    
    def to_dict(self):

        return {
            'movie_id': self.movie_id,
            'title': self.title,
            'director': self.director,
            'rating': self.rating
        }
    
    def to_json(self):

        return {
            'movie_id': self.movie_id,
            'title': self.title,
            'director': self.director,
            'rating': self.rating
        }
    
    def to_xml(self):

        return f'''<movie>

    <movie_id>{self.movie_id}</movie_id>

    <title>{self.title}</title>

    <director>{self.director}</director>

    <rating>{self.rating}</rating>

</movie>'''


