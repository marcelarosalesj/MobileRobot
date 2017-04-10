import gpiozero
from time import sleep

print "FIRST WHEEL"
print "Declaring DC motor"
# Declaring DC motor over GPIO 27 (forward) and GPIO 22 (backward)
motor = gpiozero.Motor(22, 27)

print "Let's move forward"
# Forward 2 seconds max speed
motor.forward(0.5)
sleep(2)
motor.stop()

print "Stop"

print "Let's move backward"
# Backward 2 seconds max speed
motor.backward(0.5)
sleep(2)
motor.stop()

print "Stop"

print "finish"

print "\n\n\nSECOND WHEEL"
print "Declaring DC motor"
# Declaring DC motor over GPIO 27 (forward) and GPIO 22 (backward)
motor2 = gpiozero.Motor(23, 24)

print "Let's move forward"
# Forward 2 seconds max speed
motor2.forward(0.5)
sleep(2)
motor2.stop()

print "Stop"

print "Let's move backward"
# Backward 2 seconds max speed
motor2.backward(0.5)
sleep(2)
motor2.stop()

print "Stop"

print "finish"
