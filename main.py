from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of video")
video_put_args.add_argument("likes", type=int, help="Likes on video")

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args() # will get all args from uri input
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, "/video/<int:video_id>") # registering the resource to go to this class at this uri


if __name__ == "__main__":
    app.run(debug=True) # remove debug after development