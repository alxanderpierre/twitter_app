from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.twitter_service import twitter_api
from web_app.models import db, User, Tweet

twitter_api_client = twitter_api()

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users")
@twitter_routes.route("/users.json")
def list_users():
    users = []
    user_records = User.query.all()
    for user in user_records:
        print(user)
        d = user.__dict__
        del d["_sa_instance_state"]
        users.append(d)
    return jsonify(users)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)

    twitter_user = twitter_api_client.get_user(screen_name)
    # breakpoint()
    # find or create database user:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()


    return render_template("user.html", user=db_user)
