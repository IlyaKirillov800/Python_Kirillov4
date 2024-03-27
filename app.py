from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Обработка данных и вывод результата
@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])

        feels_temperature = model.predict([[temperature, humidity]])
        return render_template('result.html', temperature=temperature, humidity=humidity, feels_temperature=feels_temperature)

if __name__ == '__main__':
    app.run(debug=True)
