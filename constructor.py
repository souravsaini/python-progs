class Complex:
	def __init__(self, r=0, i=0):
		self.real = r
		self.imag = i

	def getData(self):
		print("{0} + {1}i".format(self.real,self.imag))

c1 = Complex(10,20)
c1.getData()			