from flask import Flask
from flask_restful import Api
from Classes.Movie_class import Movie_resource
from Classes.Link_class import Link_resource
from Classes.Rating_class import Rating_resource
from Classes.Tag_class import Tag_resource

app = Flask(__name__)
api = Api(app)


api.add_resource(Movie_resource, '/movies')
api.add_resource(Link_resource, '/links')
api.add_resource(Rating_resource, '/ratings')
api.add_resource(Tag_resource, '/tags')

app.run(debug=True)
