from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'superSecretKey' # set a secret key for security purposes
# our index route will handle rendering our form


@app.route('/')
def index():
    
    if not 'count' in session:
        session['count'] = 0;
    else:
        session['count'] += int(session['incVal'])
    session['incVal'] = 1;
    return render_template("index.html")

@app.route('/countPlus1')
def countPlus1():
    print("Got Post Info")
    session['incVal'] = 1
    return redirect('/')

@app.route('/countPlus2')
def countPlus2():
    print("Got Post Info")
    session['incVal'] = 2
    return redirect('/')

@app.route('/countPlusCustom', methods=['POST'])
def countPlusCustom():
    print("Got Post Info")
    session['incVal'] = request.form['userVal']
    return redirect('/')

@app.route('/destroy')
def destroy():
    session.pop('count')	# clears all keys
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
