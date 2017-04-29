import random

class randtree:
	n = None
	edges = []
	wt = []

	def generate(self):
		grouped = [1]
		ungrouped = [i for i in range(2,self.n+1)]

		i = 0
		while(i<self.n-1):
			idx_grouped = random.randrange(0,i+1)
			idx_ungrouped = random.randrange(0,self.n-i-1)
			u = grouped[idx_grouped]
			v = ungrouped[idx_ungrouped]
			self.edges[u].append(v)
			del ungrouped[idx_ungrouped]
			grouped.append(v)
			i+=1

	def make_file(self,path):
		file = open(path,"w+")
		file.write(str(self.n)+'\n')
		for i in range(self.n+1):
			for j in range(len(self.edges[i])):
				file.write(str(i)+" "+str(self.edges[i][j])+"\n")


	def __init__(self,n):
		self.n = n
		self.edges = [[] for i in range(n+1)]
		self.generate()

