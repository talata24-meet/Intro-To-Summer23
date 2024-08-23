from flask import Flask, session, render_template, request, redirect, url_for
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCqyO79xRF8NRiV5_L5fRwRS9qu-G6V9KU",
  'authDomain': "authentication-lab-d80bb.firebaseapp.com",
  'projectId': "authentication-lab-d80bb",
  'storageBucket': "authentication-lab-d80bb.appspot.com",
  'messagingSenderId': "573605879154",
 ' appId': "1:573605879154:web:71b09e5cc8da9dcad4d1eb",
 'databaseURL':""
}

app = Flask(__name__, template_folder='templates', static_folder='static')



firebase = pyrebase.initialize_app(firebaseConfig)
auth= firebase.auth()

app.config['SECRET_KEY']='LOL'






@app.route("/signin", methods = ["GET","POST"])
def signin():
  if request.method == 'GET':
    return render_template('signin.html')
  else:
    email = request.form['email']
    password = request.form['password']
    return redirect(url_for('fortune'))
    






@app.route("/home", methods = ["GET","POST"])
def home():
    return render_template('home.html')
  


@app.route("/thanx", methods = ["GET","POST"])
def thanx():
    return render_template('thanx.html')
  




@app.route("/display", methods = ["GET","POST"])
def display():
    return render_template('display.html')
 





@app.route("/", methods = ["GET","POST"])
def sure():
  if request.method == 'GET':
    return render_template('signup.html')
  else:
    email = request.form['email']
    password = request.form['password']
    session['user'] = auth.create_user_with_email_and_password(email, password)
    session['quotes'] = []
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug = True)
