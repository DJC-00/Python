from flask import Flask
app = Flask(__name__)
@app.route('/')
def landing():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<input>')
def saySomething(input):
    return (f"Hi {input}")

@app.route('/repeat/<num>/<text>')
def repeat(num,text):
    endStr = ""
    text = text + " "
    for i in range (int(num)):
        endStr += text
    return endStr

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  