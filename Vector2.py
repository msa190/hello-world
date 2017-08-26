#encoding: utf-8
class Vector():
	v = []
	def __init__(self, w=[]):
		if(w.__class__.__name__=='int'):
			self.v = [0.0 for i in range(w)]
		else:
			self.v = w
			map(lambda x: float(x), self.v)
		
	def __len__(self):
		return len(self.v)
	
	def __getitem__(self, key):
		return self.v[key]

	def __setitem__(self, key, value):
		self.v[key] = value
	#soma
	def __add__(self, w):
		if(w.__class__.__name__!= 'Vector'):
			raise
		u = self
		k=[0.0 for i in range(u)]
		for i in range(len(u)):
			k[i] = w[i]+ u[i]
		return k
	#subtracao
	def __sub__(self,w):
		if(w.__class__.__name__!= 'Vector'):
			raise
		u = self
		k =[0.0 for i in range(u)]
		for i in range(len(u)):
			k[i]= u[i]-w[i]
		return k
	#multiplicacao por escalar
	def __mul__(self,alpha):
		#if(alpha.__class__.__name__!='Vector'):
		#raise
		u = self
		k = [0.0 for i in u]
		#map(lambda x: alpha*x, self.v)
		for i in range(len(u)):
			k[i]= u[i]*alpha
		return k
	#comutatividade da multiplicacao por escalar
	#def __rmul__(self, u):
	#	return u*self
	def escalar(self,w=[]):
		soma = 0.0
		u = self
		#if(len(u)!=len(w)):
		#	raise
		for i in range(len(u)):
			u[i] = u[i]*w[i]
		for i in range(len(u)):
			soma = soma + u[i]
		return soma
		
	def __repr__(self):
		return repr(self.v)	
