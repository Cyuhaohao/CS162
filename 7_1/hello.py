from flask import Flask, render_template, url_for,request
import random
app = Flask(__name__)

@app.route('/<facets>', methods=["POST","GET"])
def index(facets):
    if facets[-1]=="6":
        return "The number is %s" % random.randrange(1,6)
    else:
        return render_template("index.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
     app.run(debug=True)