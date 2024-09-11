from flask import Flask, render_template
import requests
from post import Post

blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(blogs_url).json()

blog_posts = []
for post in posts:
    post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    blog_posts.append(post)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = blog_posts)

@app.route('/post/<int:num>')
def show_post(num):
    clicked_post = None
    for post in blog_posts:
        if (post.id == num):
            clicked_post = post
        
    return render_template("post.html", post= clicked_post)
        

if __name__ == "__main__":
    app.run(debug=True)
