import gpiozero
from flask import Flask, render_template, request
from time import sleep
app = Flask(__name__)

devices = {
   'motor1' : {'object' : gpiozero.Motor(22, 27), 'name': 'motor1', 'state' : 'stopped'} ,
   'motor2' : {'object' : gpiozero.Motor(23, 24), 'name': 'motor2', 'state' : 'stopped' } ,
   #'servo' : {'object' : gpiozero.Servo(18), 'name':  'servo', 'state' : 'stopped' } ,
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
@app.route("/<action>")
def action(action):
   message = ""
   # Device Selection
   if action == "forward":
      #devices['servo']['object'].value = 0
      devices['motor1']['object'].forward(1)
      devices['motor2']['object'].forward(1)
      sleep(2)
      devices['motor1']['object'].stop()
      devices['motor2']['object'].stop()
      #devices['servo']['object'].value = 0
      message = "Robot moved forward."
   if action == "backward":
      #devices['servo']['object'].value = 0
      devices['motor1']['object'].backward(1)
      devices['motor2']['object'].backward(1)
      sleep(2)
      devices['motor1']['object'].stop()
      devices['motor2']['object'].stop()
      #devices['servo']['object'].value = 0
      message = "Robot moved backward."
   if action == "turnLeft":
      #devices['servo']['object'].value = -0.8
      devices['motor1']['object'].backward(1)
      devices['motor2']['object'].forward(1)
      sleep(2)
      devices['motor1']['object'].stop()
      devices['motor2']['object'].stop()
      #devices['servo']['object'].value = 0
      message = "Robot turned left."
   if action == "turnRight":
      #devices['servo']['object'].value = 0.8
      devices['motor1']['object'].forward(1)
      devices['motor2']['object'].backward(1)
      sleep(2)
      devices['motor1']['object'].stop()
      devices['motor2']['object'].stop()
      #devices['servo']['object'].value = 0
      message = "Robot turned right."
   if action == "blink":
      devices['led']['object'].blink(on_time=0.25, off_time=0.25)
      sleep(3)
      devices['led']['object'].off()
      message = "Robot blinked."
   if action == "turnLedOn":
      print "led on"
      devices['led']['object'].on()
      print "message led on"
      message = "Robot turned led on."
      print "exit led on"
   if action == "turnLedOff":
      print "led off"
      devices['led']['object'].off()
      print "message led off"
      message = "Robot turned led off."
      print "exit led off"

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'message' : message,
      'devices' : devices
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
