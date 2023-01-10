import flask_restful
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of video")
video_put_args.add_argument("likes", type=int, help="Likes on video")

videos = {}

def abort_if_video_if_doesnt_exist(video_id):
    if video_id not in videos:
        flask_restful.abort(404, message="video not found")

def abort_if_video_exists(video_id):
    if video_id in videos:
        flask_restful.abort(409, message="video already exists")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_if_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args() # will get all args from uri input
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_if_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>") # registering the resource to go to this class at this uri


if __name__ == "__main__":
    app.run(debug=True) # remove debug after development