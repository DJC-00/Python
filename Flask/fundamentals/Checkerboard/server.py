
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/', defaults={'rows': 8, 'cols': 8, 'color1': 'red', 'color2': 'black'})
@app.route('/<int:rows>', defaults={'cols': 8, 'color1': 'red', 'color2': 'black'})
@app.route('/<int:rows>/<int:cols>', defaults={'color1': 'red', 'color2': 'black'})
@app.route('/<int:rows>/<int:cols>/<color1>', defaults={'color2': 'black'})
@app.route('/<int:rows>/<int:cols>/<color1>/<color2>')
def checkerboard(rows, cols, color1, color2):
    return render_template("checkerboard.html", rows = int(rows), cols = int(cols), color1 = color1, color2 = color2)
if __name__ == "__main__":
    app.run(debug=True)