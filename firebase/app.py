from flask import Flask, session, render_template, request, redirect, url_for
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCqyO79xRF8NRiV5_L5fRwRS9qu-G6V9KU",
  'authDomain': "authentication-lab-d80bb.firebaseapp.com",
  'projectId': "authentication-lab-d80bb",
  'storageBucket': "authentication-lab-d80bb.appspot.com",
  'messagingSenderId': "573605879154",
 ' appId': "1:573605879154:web:71b09e5cc8da9dcad4d1eb",
 'databaseURL':"https://authentication-lab-d80bb-default-rtdb.firebaseio.com"
}

app = Flask(__name__, template_folder='templates', static_folder='static')



firebase = pyrebase.initialize_app(firebaseConfig)
auth= firebase.auth()
db = firebase.database()
app.config['SECRET_KEY']='LOL'






@app.route("/signin", methods = ["GET","POST"])
def signin():
  if request.method == 'GET':
    return render_template('signin.html')
  else:
    email = request.form['email']
    password = request.form['password']
    return redirect(url_for('home'))
 

@app.route("/signout", methods = ["GET","POST"])
def signout():
  return redirect(url_for('signin'))
  
  
  
  
  
@app.route("/home", methods = ["GET","POST"])
def home():
  if request.method == "POST":
    messages = request.form['msg']
    session["quotes"]="msg"
    return redirect(url_for('thanx'))
  else:
    return render_template('home.html')
  


@app.route("/thanx", methods = ["GET","POST"])
def thanx():
  return render_template('thanx.html')
  




@app.route("/display", methods = ["GET","POST"])
def display():
  quote = session.get("quotes", [])
  return render_template('display.html', quote = quote)
 





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
