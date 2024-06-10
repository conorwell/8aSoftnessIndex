from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class UserModel(db.Model):
    username = db.Column(db.String(25), nullable=False, primary_key=True)
    softnessScore = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"User(username={UserModel.username}, softnessScore= {UserModel.softnessScore})"


usernames = {"conor-wellman": 0.09,
             "ben-blackmore":0.07}

resource_fields = {
    'username' : fields.String,
    'softnessScore' : fields.Float
}

class getIndex(Resource):

    @marshal_with(resource_fields)
    def get(self,username):
        result = UserModel.query.filter_by(username=username).first()
        if not result:
            abort(404, message="Could not find user")
        else:
            return result

    @marshal_with(resource_fields)
    def post(self,username):
        result = UserModel.query.filter_by(username=username).first()
        if result:
            abort(409,message="username already calculated")
        else:
            #calculate score here
            score = 0.1
            user = UserModel(username = username, softnessScore = score)
            db.session.add(user)
            db.session.commit()
            return user, 201

    @marshal_with(resource_fields)
    def patch(self,username):
        result = UserModel.query.filter_by(username=username).first()
        if not result:
            abort(404, message="Could not find user")
        else:
            # calculate new score
            score = 0.5
            result.softnessScore = score
            db.session.commit()
            return result

api.add_resource(getIndex, "/getIndex/<string:username>")

if __name__ == "__main__":
    #turn off debug for prod env
    app.run(debug = True)