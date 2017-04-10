import gpiozero
from time import sleep

print "Declare motors"
# Declaring motors on GPIOs 22, 27, 23 and 24. These are for moving f/b.
motor1 = gpiozero.Motor(22, 27)
motor2 = gpiozero.Motor(23, 24)
# Declaring servomotor on GPIO 18. This will give direction.
servo = gpiozero.Servo(18)

print "First routine"
# First routine. Robot move forward.
servo.mid()
motor1.forward(1) # Max speed
motor2.forward(1) # Max speed
print "About to sleep"
sleep(5)
print "Stopping motors"
motor1.stop()
motor2.stop()


print "Finish"
