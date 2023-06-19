from flask import Flask, render_template, request
import random
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app) # tie app to bootstrap

@app.route("/")
def index():
    my_dict = {"insert_something1":"This is insert_something1",
               "insert_something2": "This is insert_something2",
               "test_titles":["title1", "title2", "title3"]
               }

    return render_template("testapp/index.html", my_dict = my_dict)

@app.route("/sampleform", methods=["GET", "POST"])
def sampleform():
    if request.method =="GET":
        return render_template("sampleform.html")

    if request.method =="POST":
        comp = random.randrange(3)
        if comp == 0:
            comp_hand = "Computer is Stone"
        elif comp == 1:
            comp_hand = "Computer is Scissors"
        else:
            comp_hand = "Computer is Paper"

        req1 = int(request.form["janken"])

        if req1 == 0:
            your_hand = 'You are Stone'
        elif req1 == 1:
            your_hand = 'You are Scissors'
        else:
            your_hand = 'You are Paper'

        if comp == req1:
            result = "draw"
        elif req1 == 1 and comp ==0:
            result ="You lose"

        elif req1 == 2 and comp ==0:
            result ="You win"

        elif req1 == 0 and comp ==1:
            result ="You win"

        elif req1 == 2 and comp ==1:
            result ="You lose"

        elif req1 == 0 and comp == 2:
            result ="You lose"

        elif req1 == 1 and comp == 2:
            result ="You win"

        judge ={
            "computer_hand":comp_hand,
            "player_hand":your_hand,
            "judgement":result,
        }

    return render_template("janken_result.html", judge=judge)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)