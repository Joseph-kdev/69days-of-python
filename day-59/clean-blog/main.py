from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

DATA_SOURCE = "https://api.npoint.io/a51b7b87232739be5dfc"

blogs = []
blogs_data = requests.get(DATA_SOURCE).json()

for blog in blogs_data:
    blogs.append(blog)

@app.route('/')
def home():
    return render_template("index.html", blogs = blogs)

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def post(index):
    picked_blog = None
    for blog in blogs:
        if blog["id"] == index:
            picked_blog = blog
        
    return render_template("post.html", index = index, blog_piece = picked_blog)

if __name__ == "__main__":
    app.run(debug=True)