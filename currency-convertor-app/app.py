from flask import Flask, render_template,request

import requests
import json

app=Flask(__name__)

#restful API function and by passing these parameters so in route will get these parameters through request.form
#once we get them from request.form will pass them throug  querystring dict
#then will get json syntax of 3 values , will take just the amount and round it 2 decimal places
def get_currency(from_,to_,amt):
    url = "https://currency-converter13.p.rapidapi.com/convert"
    querystring = {"from":from_,"to":to_,"amount":amt}
    headers = {
    'x-rapidapi-key': "bbc4e72c95msh764d7107571c9ccp132292jsne000b3620c23",
    'x-rapidapi-host': "currency-converter13.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    print("***********************",response)
    final_result=round(response["amount"],2)
    return final_result

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert",methods=['POST'])
def convert_currency():
    from_curency=request.form['change_from']#will get user input
    to_curency=request.form['change_to']
    amount=request.form['amount']
    result=get_currency(from_curency,to_curency,amount)#will call the function that has the result
    return render_template('index.html',result=result)#will pass the result to html page via jinja syntax to get it displayed in webpage


if(__name__)=="__main__":
    app.run(debug=True)