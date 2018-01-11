import gpiozero
from time import sleep

print "creating motor objects"

# back motors
br = gpiozero.Motor(22, 27) # back right
bl = gpiozero.Motor(23, 24) # back left

# front motors
fr = gpiozero.Motor(12,16) # front right
fl = gpiozero.Motor(6,5) # front left


print "finish"
