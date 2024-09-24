from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

class login_form(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="Please enter a value"), Email(message="Invalid email address")])
    password = PasswordField(label='Password', validators=[DataRequired(message="Please enter a value"), Length(min=8, message=f"Password must be at least 8 characters")])
    submit = SubmitField(label='Log In')
    

app = Flask(__name__)
Bootstrap(app=app)
app.secret_key = 'mysecretkey'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form= form)

if __name__ == '__main__':
    app.run(debug=True)