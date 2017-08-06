from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)
app.secret_key="JADE"

@app.route('/')
def index():
	try:
		isinstance(session['random'],int)==True
	except:
		session['random']=random.randrange(0, 101)
	# print session['random']
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	hold=request.form['guess']
	if session['random']-int(hold)==0:
		print "hello"
	return redirect('/')
app.run(debug=True)