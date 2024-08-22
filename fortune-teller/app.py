from flask import Flask,render_template, request, redirect, url_for
import random

app = Flask(__name__,
template_folder="templates",
static_folder="static")

@app.route("/home", methods = ["GET","POST"])
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		name = request.form['firstname']
		birth_month = request.form['birthmonth']
		animal = request.form['animal']
       
		return redirect(url_for('fortune',
            b = birth_month))
            

	return render_template("home.html")

@app.route("/fortune/<string:b>",methods=["GET","POST"])
def fortune(b):
	fortunes = ["Do not be afraid of competition.", 
	"An exciting opportunity lies ahead of you.", 
	"You love peace.",
	"You will always be surrounded by true friends.",
	"Sell your ideas-they have exceptional merit.",
	"You should be able to undertake and complete anything.",
	"You are kind and friendly.",
	"You are wise beyond your years.","Your ability to juggle many tasks will take you far.",
	"You will be happy with your spouse."
	]

	lol = len(b)
	return render_template("fortune.html",fortune = fortunes[lol-1])





	# random.choice(fortunes)
	# fortune= random.choice(fortunes)
	#fortune=random.choice(fortunes))
if __name__ == "__main__":
	app.run(debug = True )