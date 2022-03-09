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
    for i in range(len(input)):
            if (str.isdigit(input[i])):
                return "Invalid Input: Input argument contains a number "
    return (f"Hi {input}")

@app.route('/repeat/<num>/<text>')
def repeat(num,text):
    if (str.isdigit(num)):
        for i in range(len(text)):
            if (str.isdigit(text[i])):
                return "Invalid Input: Second argument contains a number "
        endStr = ""
        text = text + " "
        for i in range (int(num)):
            endStr += text
        return endStr
    return (f"invalid Input: First argument is not a number")

@app.route('/<route>')
def invalid(route):
    return "This is not a valid path"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  