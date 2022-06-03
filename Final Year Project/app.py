from sensor import Sensor
from flask import Flask, render_template, request
app = Flask(__name__)

Sensors = Sensor()

#DB 
#If DB connected 
#Run Flask 

@app.route("/" , methods=['GET', 'POST'])
def index():
    temperature = Sensors.Sensor_1()
    speed = Sensors.Sensor_2()
    rpm = Sensors.Sensor_3()
    range = Sensors.Sensor_4()
    energy = Sensors.Sensor_5()
    return render_template("home.html",temperature=temperature,speed = speed, rpm = rpm, range = range,energy = energy)

if __name__== '__main__':
    app.run(debug = True)
