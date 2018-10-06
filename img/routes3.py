from flask import Flask, request, render_template, jsonify
import json
import numpy as np
from sklearn.externals import joblib
import pickle
#logre=joblib.load('jsonmodel.pkl')

ip=open("sri",'rb')
m=pickle.load(ip)
h=0
w=0
ge=""
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('example.html')

@app.route('/submit',methods=['POST'])
def fun():
	if request.method == 'POST':
		data=request.form
		global h
		h=float(request.form['height'])
		global w
		w=float(request.form['weight'])
		global ge
		ge=request.form['gender']
		if ge=='male':
			return render_template('home2.html')
		else:
			return render_template('home.html')	

@app.route('/Submit',methods=['POST'])
def Submit():
	if request.method == 'POST':
		print("hello")		
		data=request.form
		print(data)
		if ge=='male':
			preg=0
		else:
			preg = int(request.form['Pregnancies'])
		print(preg)
		gluc = float(request.form['Glucose'])
		bp = float(request.form['BloodPressure'])                
		st = float(request.form['SkinThickness'])                
		iss = float(request.form['Insulin'])
		hi=0.3048*h                
		bmi= w/(hi*hi)  
		print(bmi)              
		dpf=float(request.form['DiabetesPredigreeFunction'])                		
		age=int(request.form['Age'])
		k=[[preg,gluc,bp,st,iss,bmi,dpf,age]]                
		pred=m.predict(k) 
		if pred == [0.]:
			p="NEGATIVE"
		else:
			p="POSITIVE"


		if p=="POSITIVE":
			return render_template('res1.html')
		else:
			return render_template('result.html')
		#return "hello"


if __name__ == '__main__':
  app.run(debug=True)
