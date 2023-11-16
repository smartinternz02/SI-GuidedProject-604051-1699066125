# pip install flask

from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np

model=pickle.load(open('model.pkl','rb'))

app= Flask(__name__)  # your application


@app.route('/')  # default route 
def home():
    return render_template('home.html') # rendering if your home page.

@app.route('/pred',methods=['POST']) # prediction route
def predict1():
    '''
    For rendering results on HTML 
    '''
    
    a1 = request.form["step"]
    a2= request.form["amount"]
    a3 = request.form["oldbalanceOrg"]
    a4= request.form["newbalanceOrig"]
    a5= request.form["oldbalanceDest"]
    a6= request.form["newbalanceDest"]
    a7= request.form["type_CASH_OUT"]
    a8= request.form["type_DEBIT"]
    a9= request.form["type_PAYMENT"]
    a10= request.form["type_TRANSFER"]

    t =  [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]

    for i in range(len(t)):
        t[i]=float(t[i])
    t=np.reshape(t,[1,-1])
    output =model.predict(t)
    print(output)
    if output==1:
        return render_template("home.html", result = "The payement is safe  ")
    else:
        return render_template("home.html", result = "The payement is fraud and not safe  ")
    
    
    
# running your application
if __name__ == "__main__":
    app.run()

#http://localhost:5000/ or localhost:5000

