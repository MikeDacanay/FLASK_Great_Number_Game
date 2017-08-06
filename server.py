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
	print session['random']
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	if session['random']==int(request.form['guess']):
		passhint="right on"
		session['random']=random.randrange(0, 101)
	elif session['random']>int(request.form['guess']):
		passhint="more"
	elif session['random']<int(request.form['guess']):
		passhint="less"
	return render_template('index.html',hint=passhint)

app.run(debug=True)