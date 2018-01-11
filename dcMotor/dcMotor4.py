import gpiozero
from time import sleep

print "creating motor objects"

# atras derecho e izquierdo
ad = gpiozero.Motor(22, 27)
ai = gpiozero.Motor(23, 24)

# frente derecho e izquierdo
fd = gpiozero.Motor(12,16)
fi = gpiozero.Motor(5,6)


print "finish"
