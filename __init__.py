from flask import Flask, render_template, jsonify
from urllib.request import urlopen
import json
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/submit_message/", methods=["POST"])
def submit_message():
    # Traitement de la soumission du formulaire (non implémenté dans cet exercice)
    return "Message soumis avec succès!"

@app.route('/paris/')
def meteo():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=bd5e378503939ddaee76f12ad7a97608')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('temp', {}).get('day') - 273.15  # Conversion de Kelvin en °C
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def histogramme():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=bd5e378503939ddaee76f12ad7a97608')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('temp', {}).get('day') - 273.15  # Conversion de Kelvin en °C
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    
    print(results)  # Imprimez les données récupérées
    
    return render_template("histogramme.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)

