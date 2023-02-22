import requests
from flask import Flask, render_template

app = Flask(__name__)
INDEX_HTML = "index.html"
POST_HTML = "post.html"
BLOG_API = "https://api.npoint.io/c790b4d5cab58020d391"
HOME_PATH = '/'
POST_ID_KEY = "id"
SHOW_POST_PATH = "/path/<int:index>"
blog_response = requests.get(BLOG_API)
blog_posts = blog_response.json()


@app.route(HOME_PATH)
def home():
    return render_template(INDEX_HTML, posts=blog_posts)


@app.route(SHOW_POST_PATH)
def show_post(index):
    requested_post = None
    for post in blog_posts:
        if index == post[POST_ID_KEY]:
            requested_post = post
    return render_template(POST_HTML, blog_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
