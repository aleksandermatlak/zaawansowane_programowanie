from flask_restful import Resource
import csv
import json


class Movie:
    def __init__(self, mid: int, title: str, genres: str):
        self.id = mid
        self.title = title
        self.genres = genres

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


def get_movies():
    movies: list[Movie] = []
    with open('data/movies.csv', newline='', encoding='UTF-8') as file:
        file.readline()
        reader = csv.reader(file)
        for row in reader:
            movie_id = int(row[0])
            movie_title = row[1]
            movie_genre = row[2]
            movie = Movie(movie_id, movie_title, movie_genre)
            movies.append(movie.__dict__)
    return movies


class Movie_resource(Resource):
    def get(self):
        return get_movies()
