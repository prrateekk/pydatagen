import random

class randgraph:
	n = None
	m = None
	edges = []
	taken = {}

	def generate(self):
		i = 0
		while i<self.m:
			u = random.randrange(1,self.n+1)
			v = random.randrange(1,self.n+1)
			while u==v:
				v = random.randrange(1,self.n+1)
			if u>v:
				u,v = v,u
			if (u,v) in self.taken:
				continue
			else:
				self.taken[(u,v)] = 1
				self.edges[u].append(v)
				i+=1


	def make_file(self,path):
		file = open(path,"w+")
		file.write(str(self.n)+'\n')
		for i in range(self.n+1):
			for j in range(len(self.edges[i])):
				file.write(str(i)+" "+str(self.edges[i][j])+"\n")


	def __init__(self,n,m):
		self.n = n
		self.m = m
		self.edges = [[] for i in range(n+1)]
		self.generate()
