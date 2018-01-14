import gpiozero
from time import sleep

print "r4w movement library"


class Robot():

	# back motors
	br = gpiozero.Motor(22, 27) # back right, connected to rpi BCM 27 and 22
	bl = gpiozero.Motor(23, 24) # back left, connected to rpi BCM 23 and 24
	# front motors
	fr = gpiozero.Motor(12,16) # front right, connected to rpi BCM 12 and 16
	fl = gpiozero.Motor(6,5) # front left, connected to rpi BCM 6 and 5
	opt = gpiozero.Button(17) # opt is the optocoupler that is measuring encoder in back-left wheel, the encoder has 20 holes 
	counter = 0 # variable needed to count up to the 20 holes in the step function 
	
	print "created motors"

	def __init__(self):
		print "created class"

	def forward(self, speed=1):
		"""
	
		"""
		print "forward ", speed
		self.br.forward(speed)
		self.bl.forward(speed)
		self.fr.forward(speed)
		self.fl.forward(speed)

	def backward(self, speed=1):
		print "backward ", speed
		self.br.backward(speed)
		self.bl.backward(speed)
		self.fr.backward(speed)
		self.fl.backward(speed)

	def stop(self):
		print "stop"
		self.br.stop()
		self.bl.stop()
		self.fr.stop()
		self.fl.stop()

	
	def right(self, degrees=90):
		self.counter = 0
                def count_one():
                        self.counter = self.counter + 1
                        print " counter is ", self.counter
                self.opt.when_pressed = count_one
		
		# Turning Right Movement
                self.fl.forward(1)
		self.bl.forward(1)
		self.fr.backward(1)
		self.br.backward(1)

                while self.counter < 10:
                        sleep(1.0/1000000.0)
                self.stop()

	def left(self):
		self.fl.backward(1)
		self.bl.backward(1)
		self.fr.forward(1)
		self.br.forward(1)
		sleep(1)
		self.stop()


	
	def step(self, direction):
		self.counter = 0
		def count_one():
			self.counter = self.counter + 1
			print " counter is ", self.counter

		self.opt.when_pressed = count_one

		if direction == "f":
			self.forward(1)
		elif direction == "b":
			self.backward(1)
		else:
			self.forward(1) # for now the default is forward, this function may throw an error later

		while self.counter < 20:
			sleep(1.0/1000000.0)
		self.stop()


	def steps_forward(self, num_steps=1):
		for i in range(0,num_steps):
			self.step("f")

	def steps_backward(self, num_steps=1):
		for i in range(0, num_steps):
			self.step("b")

