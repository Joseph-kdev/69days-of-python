from flask import Flask
import random

app = Flask(__name__)


number = random.randint(0, 9)
@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDM0ajBjcTJncjBncHF2NW4wNjU3NTB5d2lqaTI3YTN1ZXdwYmU2dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ne3xrYlWtQFtC/giphy.gif">'
            
@app.route("/<int:guess>")
def guess_number(guess):
    if guess == number:
        return '<h1 style="color: green">You found me!</h1>'\
                '<img src="https://media.giphy.com/media/RlAzoSsoDPt6ezkgLY/giphy.gif?cid=ecf05e47bmbuj7z07sr9mfedf8aylh1rkf8ne076pnly8cw3&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    elif guess > number:
        return '<h1 style="color: red">Too high, try again!</h1>'\
                '<img src="https://media.giphy.com/media/2cei8MJiL2OWga5XoC/giphy.gif?cid=ecf05e47mwktt8zwcssapf814u7ql7vcwibzp7j9iyjhvtun&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    elif guess < number:
        return '<h1 style="color: purple">Too low, try again!</h1>'\
                '<img src="https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif?cid=790b7611wxjcqiaj6veh6nr3ipl45yhl17afsj2bw4kfekr3&ep=v1_gifs_search&rid=giphy.gif&ct=g">'


if __name__ == "__main__":
    app.run(debug=True)