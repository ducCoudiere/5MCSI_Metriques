from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen 
import sqlite3 
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                        
@app.route('/') 
def hello_world():
    return render_template('hello.html')

#@app.route("/contact/")
#def MaPremiereAPI():
    #return "<h2>Ma page de contact</h2>"


#@app.route("/contact/")
#def MaPremiereAPI():
 #return render_template("formulaire.html")

@app.route("/booking/")
def MaPremiereAPI():
    return render_template("booking.html")

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("formulaire2.html")

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results) 



@app.route('/commits/data')
def get_commits_data():
    url = 'https://api.github.com/repos/ducCoudiere/5MCSI_Metriques/commits'
    response = urlopen(url)
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    
    commit_minutes = []
    for commit in json_content:
        date_string = commit['commit']['author']['date']
        date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
        commit_minutes.append(date_object.minute)
    
    return jsonify(commit_minutes=commit_minutes)
 

@app.route("/commits/")
def commits():
    return render_template("commits.html")

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")

if __name__ == "__main__":
  app.run(debug=True)
 
