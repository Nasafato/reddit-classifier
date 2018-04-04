import praw
import os
from praw.models import MoreComments

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    reddit = praw.Reddit(client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent='testscript by /u/nasafato')

    subreddit = reddit.subreddit('cscareerquestions')

    data = []
    for submission in subreddit.hot(limit=2):
        data.extend([top_level_comment for top_level_comment in submission.comments])

    return render_template('index.html', data=data)
