#Nicole Hendry
#Understanding Routing

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hi(name):
    name = str(name)
    print(name)
    return "Hi " + name + "!"

@app.route('/repeat/<numb>/<word>')
def repeat(numb, word):
    numb = int(numb)
    word = str(word)
    return (word + " " )*numb

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__": 
    app.run(debug=True) 