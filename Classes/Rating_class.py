from flask_restful import Resource
import csv
import json


class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.timestamp = timestamp
        self.rating = rating
        self.movie_id = movie_id
        self.user_id = user_id

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


def get_ratings():
    ratings: list[Rating] = []
    with open('data/ratings.csv', newline='', encoding='UTF-8') as file:
        file.readline()
        reader = csv.reader(file)
        for row in reader:
            user_id = int(row[0])
            movie_id = row[1]
            rating = row[2]
            timestamp = row[3]
            rating = Rating(user_id, movie_id, rating, timestamp)
            ratings.append(rating.__dict__)
    return ratings


class Rating_resource(Resource):
    def get(self):
        return get_ratings()