from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    if request.form['name']:
        session['username'] = request.form['name']
    else:
        session['username'] = "Jane"
    if request.form['location']:
        session['userLocation'] = request.form['location']
    else:
        session['userLocation'] = "Doe"

    if request.form['language']:
        session['userLang'] = request.form['language']
    if 'frameworks' in request.form:
        session['userFrWk'] = request.form.getlist('frameworks')
    else:
        session['userFrWk'] = "none"
    if 'hearFrom' in request.form:
        session['userHeFr'] = request.form['hearFrom']
    else:
        session['userHeFr'] = "none"
    return redirect('/result')


    
# adding this method
@app.route('/result')
def showResult():
    return render_template('result.html')

@app.route('/reset')
def reset():
    session.clear();
    return redirect('/')

    
if __name__ == "__main__":
    app.run(debug=True)

