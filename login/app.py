import sqlite3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/base')
def base():
  return render_template('base.html')

@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    return render_template('login.html') 

@app.route('/portfolio', methods=['GET', 'POST']) 
def portfolio(): 
    return render_template('portfolio.html') 

@app.route('/submit_details', methods=['GET', 'POST']) 
def submit_details(): 
    return redirect(url_for('index')) 

@app.route('/view_contacts', methods=['GET']) 
def view_contacts(): 
    contacts = "" 
    return render_template('contacts.html', contacts=contacts)

if __name__ == "__main__":
  app.run(debug=True)