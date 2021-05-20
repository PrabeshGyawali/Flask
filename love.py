from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    First_name = [2, 4, 6 ]
    listo = 6
    warning = "The page is full"
    return render_template("index.html")
@app.errorhandler(404)
def Page_not_found(e):
    return render_template("index.html"), 404



app.run(debug=True)


