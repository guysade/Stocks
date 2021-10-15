from os import system
from flask import Flask
import flask
from flask import Flask, render_template, redirect, request, jsonify
from werkzeug import datastructures
import requests
import json
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('index.html') 

@app.route('/get_ticker_summary', methods = ['POST'])
def keyStats():
    try:
        ticker = request.form.get('ticker')
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+ticker+'&apikey=O8R5LTK0O37K7G5J'
        r = requests.get(url)
        quote = r.json()

        statsURL = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+ticker+'&apikey=O8R5LTK0O37K7G5J'
        k = requests.get(statsURL)
        keystats = k.json()
        
        cashURL = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol='+ticker+'&apikey=O8R5LTK0O37K7G5J'
        c = requests.get(cashURL)
        cashflow = c.json()

        quote = quote['Global Quote']
        cashflow = cashflow['quarterlyReports'][0]['operatingCashflow']
    except:
        return redirect('/404')
    
    return flask.render_template('newkeystats.html', keystats = keystats, quote = quote, cashflow = cashflow, ticker = ticker)

@app.route('/csv', methods = ['POST'])
def downloadCSV():
    a = request.form.to_dict()
    ticker = list(a.keys())[0]
    print(ticker)
    csvurl = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+ticker+'&apikey=O8R5LTK0O37K7G5J&datatype=csv'
    return redirect(csvurl)

@app.route('/404')
def error():
    return flask.render_template('404.html') 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
