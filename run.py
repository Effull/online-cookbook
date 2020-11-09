import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_title="Home")

@app.route("/breakfast")
def breakfast():
    return render_template("breakfast.html", page_title="Breakfast")

@app.route("/lunch")
def lunch():
    return render_template("lunch.html", page_title="Lunch")

@app.route("/dinner")
def dinner():
    return render_template("dinner.html", page_title="Dinner")


#CHANGE DEBUG TO FALSE WHEN DONE
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )