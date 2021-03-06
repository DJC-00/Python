
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return("Home Page!")

@app.route('/list')
def list():
    users = [
        {'number' : 1, 'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'number' : 2, 'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'number' : 3, 'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'number' : 4, 'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("list.html", userList = users)

if __name__ == "__main__":
    app.run(debug=True)