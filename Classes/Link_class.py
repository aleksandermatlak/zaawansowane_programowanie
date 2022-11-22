from flask_restful import Resource
import csv
import json


class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.tmdb_id = tmdb_id
        self.imdb_id = imdb_id
        self.movie_id = movie_id

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


def get_links():
    links: list[Link] = []
    with open('data/links.csv', newline='', encoding='UTF-8') as file:
        file.readline()
        reader = csv.reader(file)
        for row in reader:
            movie_id = int(row[0])
            imdb_id = row[1]
            tmdb_id = row[2]
            link = Link(movie_id, imdb_id, tmdb_id)
            links.append(link.__dict__)
    return links


class Link_resource(Resource):
    def get(self):
        return get_links()
