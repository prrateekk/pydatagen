import random

class randlist:
	n = None
	l = None
	r = None
	array = []

	def generate(self):
		self.array = []
		for i in range(self.n):
			self.array.append(random.randrange(self.l,self.r))

	def make_file(self,path,connect=' '):
		file = open(path,"w+")
		file.write(str(self.n)+'\n')
		file.write(connect.join(str(x) for x in self.array))
		file.close()

	def __init__(self,n,l,r):
		self.n = n
		self.l = l
		self.r = r+1
		self.generate()

