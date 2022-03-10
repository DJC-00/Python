
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/makebox', defaults={'boxColor': 'Blue', 'boxNum': 3})
@app.route('/makebox/<boxColor>', defaults={'boxNum': 3})
@app.route('/makebox/<boxColor>/<boxNum>')
def makeBox(boxColor, boxNum):
    return render_template("makeBox.html", boxNum = int(boxNum), boxColor = boxColor)
if __name__ == "__main__":
    app.run(debug=True)