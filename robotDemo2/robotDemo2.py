# based on http://mattrichardson.com/Raspberry-Pi-Flask/
import gpiozero
from flask import Flask, render_template, request
from time import sleep
app = Flask(__name__)

devices = {
   'motor1' : {'object' : gpiozero.Motor(22, 27), 'name': 'motor1', 'state' : 'stopped'} ,
   'motor2' : {'object' : gpiozero.Motor(23, 24), 'name': 'motor2', 'state' : 'stopped' } ,
   'servo' : {'object' : gpiozero.Servo(18), 'name':  'servo', 'state' : 'stopped' } ,
   'led' : {'object' : gpiozero.DigitalOutputDevice(25), 'name': 'led', 'state' : 'off' }
   }

@app.route("/")
def main():
   # Put data in templateData
   templateData = {
      'devices' : devices
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<device>/<action>")
def action(device, action):
   # Get device object
   changeDevice = devices[device]['object']
   deviceName = device

   # Device Selection
   if action == "forward":
      changeDevice.forward(1)
      sleep(2)
      changeDevice.stop()
      message = deviceName + " moved forward."
   if action == "backward":
      changeDevice.backward(1)
      sleep(2)
      changeDevice.stop()
      message = deviceName + " moved backward."
   if action == "max":
      changeDevice.max()
      message = deviceName + " moved max"
   if action == "mid":
      changeDevice.mid()
      message = deviceName + " moved mid."
   if action == "min":
      changeDevice.min()
      message = deviceName + " moved min."
   if action == "on":
      changeDevice.on()
      message = "Turned " + deviceName + " on."
   if action == "off":
      changeDevice.off()
      message = "Turned " + deviceName + " off."

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'message' : message,
      'devices' : devices
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
