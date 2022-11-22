from flask_restful import Resource
import csv
import json


class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.timestamp = timestamp
        self.tag = tag
        self.movie_id = movie_id
        self.user_id = user_id

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


def get_tags():
    tags: list[Tag] = []
    with open('data/tags.csv', newline='', encoding='UTF-8') as file:
        file.readline()
        reader = csv.reader(file)
        for row in reader:
            user_id = int(row[0])
            movie_id = row[1]
            tag = row[2]
            timestamp = row[3]
            new_tag = Tag(user_id, movie_id, tag, timestamp)
            tags.append(new_tag.__dict__)
    return tags


class Tag_resource(Resource):
    def get(self):
        return get_tags()
