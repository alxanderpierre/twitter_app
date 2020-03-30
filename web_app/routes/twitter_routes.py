from flask import Blueprint, render_template

from web_app.twitter_service import twitter_api
from web_app.models import db, User, Tweet

twitter_api_client = twitter_api()

twitter_routes = Blueprint("twitter_routes", __name__)


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
