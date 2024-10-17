from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


MY_TMDB_KEY = "some key"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap(app)
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
    
class Editform(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")
    
class AddMovie(FlaskForm):
    title = StringField(label="Enter Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")
    
@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
        
    db.session.commit()
    return render_template("index.html", movies = movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={MY_TMDB_KEY}&query={movie_title}")
        data = response.json()["results"]
        return render_template("select.html", options = data)
    return render_template("add.html", form=form)

@app.route("/details")
def get_details():
    movie_api_id = request.args.get("id")
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_api_id}?api_key={MY_TMDB_KEY}&language=en-US")
    data = response.json()
    new_movie = Movie(
        title = data["title"],
        year = data["release_date"].split("-")[0],
        description = data["overview"],
        img_url = f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id = new_movie.id))

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = Editform()
    movie_id = request.args.get("id")
    movie_to_edit = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_edit.rating = float(form.rating.data)
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=form, movie= movie_to_edit)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
