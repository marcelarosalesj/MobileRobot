from gpiozero import LED, Button
from time import sleep
from random import uniform

# Define components
print "Starting the game"
led = LED(4)
right_button = Button(15)
left_button = Button(14)

print "Turn on"
led.on()
sleep(uniform(5 , 10))
led.off()
print "Turn off"


def pressed(button):
    print "Button Pressed: ", button.pin.number

# Assign function to buttons
right_button.when_pressed = pressed
left_button.when_pressed = pressed

# Wait
sleep(3)

print "finish"
