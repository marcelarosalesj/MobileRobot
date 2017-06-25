# based on http://mattrichardson.com/Raspberry-Pi-Flask/
import gpiozero
from flask import Flask, render_template, request
app = Flask(__name__)

devices = {
   25 : {'object' : gpiozero.DigitalOutputDevice(25), 'name': 'led' }
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
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int( filter( str.isdigit, str(changePin) ) )
   # Get the device name for the pin being changed:
   deviceName = devices[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      devices[changePin]['object'].on()
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      devices[changePin]['object'].off()
      message = "Turned " + deviceName + " off."
   if action == "toggle":
      # Read the pin and set it to whatever it isn't (that is, toggle it):
      devices[changePin]['object'].toggle()
      message = "Toggled " + deviceName + "."

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'message' : message,
      'devices' : devices
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
