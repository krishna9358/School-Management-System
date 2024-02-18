import requests
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('login.html' )

@app.route("/teacher")
def teacher ():
    return render_template('teacher.html')

@app.route("/login" , methods= ['GET', 'POST'])
def login():
    return render_template ('login.html')

@app.route("/signup", methods= ['GET', 'POST'])
def signup():
    return render_template ('signup.html')

@app.route("/student")
def student():
    return render_template('student.html')

@app.route("/principal")
def principal():
    return render_template('principal.html')

@app.route("/library")
def library():
    return render_template ('library.html')

@app.route('/forgotPass')
def forgotPass():
	return render_template('forgotPass.html')

app.run()
