from flask import Flask, render_template

app = Flask(__name__)

""" An Example of routing in flask application """
@app.route("/")
def index():
  return 'Hello World!'

@app.route("/home")
def home():
   return render_template("home.html")

@app.route("/sanju")
def sanju():
   return 'Hi! Sanju is here'

@app.route("/greetings/<name>")
def greetings(name):
   return 'Good Morning ' + name + "!!"

@app.route("/square/<int:n>")
def square(n):
   return "square of number {} is : {}".format(n, n*n) 

@app.route("/sum/<float:a>/<float:b>")
def sum(a, b):
   return "sum is {}".format(a+b)

if __name__ == '__main__':
   app.run(debug = True, host = "0.0.0.0", port = 3000)
   app.run()


   