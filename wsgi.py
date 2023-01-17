from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from codecarbon import EmissionsTracker
from codecarbon import track_emissions


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %s>' % self.title


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)

    def post(self):
        new_post = Post(
            title=request.json['title'],
            content=request.json['content']
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)


class PostResource(Resource):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post_schema.dump(post)

    def patch(self, post_id):
        post = Post.query.get_or_404(post_id)

        if 'title' in request.json:
            post.title = request.json['title']
        if 'content' in request.json:
            post.content = request.json['content']

        db.session.commit()
        return post_schema.dump(post)

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204

class HealthResource(Resource):
    @track_emissions
    def get(self):
        print('We track the emission of all the command of the endpoint')
        return 200

class PartialTrackResource(Resource):
    def get(self):
        tracked_list = []
        for i in range(1_000_000):
            tracked_list.append(i)
        print('Non tracked operations: Added 1_000_000 to a list')

        with EmissionsTracker() as tracker:
            print('We track the emission only of the commands inside the tracker')
            tracked_list = []
            for i in range(1_000_000):
                    tracked_list.append(i)
            print('Tracked operations: Added 1_000_000 to a list')
        return 204

class EndpointTrackResource(Resource):
    @track_emissions
    def get(self):
        print('We track the emission of all the command of the endpoint')
        numeric_list = []
        for i in range(1_000_000):
            numeric_list.append(i)
        print('Added 1_000_000 to a list')
        return 204

api.add_resource(PostListResource, '/posts')
api.add_resource(HealthResource, '/health')
api.add_resource(PartialTrackResource, '/partial-track')
api.add_resource(EndpointTrackResource, '/endpoint-track')
api.add_resource(PostResource, '/posts/<int:post_id>')


if __name__ == '__main__':
    app.run(debug=True)
