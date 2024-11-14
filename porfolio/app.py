from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """
    Landing page

    """

    return render_template("home.html")


@app.route("/tinotenda")
def tinotenda_portfolio():
    return render_template("tinotenda.html")


@app.route("/nicholas")
def nicholas_portfolio():
    return render_template("nicholas.html")


@app.route("/candace")
def candace_portfolio():
    return render_template("candace.html")


@app.route("/eddy")
def eddy_portfolio():
    return render_template("eddy.html")


@app.route("/oheneba")
def oheneba_portfolio():
    return render_template("oheneba.html")

@app.route("/extra")

def extra_porfolio():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
