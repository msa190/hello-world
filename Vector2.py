#encoding: utf-8
#import copy
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
		u = self
		if(w.__class__.__name__!= 'Vector'):
			raise
		#u = copy.deepcopy(self)		
		k = [0.0 for i in range(4)]
			
		for i in range(len(u)):
			k[i] = w[i]+ u[i]
			#u[i] = w[i]+ u[i]
		return k
	#subtracao
	def __sub__(self,w):
		u = self
		if(w.__class__.__name__!= 'Vector'):
			raise
			#else raise		
		k = [0.0 for i in u]
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
		k = [0.0 for i in u]
		#if(len(u)!=len(w)):
		#	raise
		for i in range(len(u)):
			k[i] = u[i]*w[i]
		for i in range(len(k)):
			soma = soma + k[i]
		return soma
		
	def __repr__(self):
		return repr(self.v)
#x_product ainda não testado
def x_product(w=[],v=[]):
	a = w
	b = v
	#if len(w) == 2:
	#	for i,j in w:
	#		a[j] = i
	#	a[3] = 0.0
	#if len(v) == 2:
	#	for i, j in v:
	#		b[j] = i
	#	b[3] = 0.0
	c = [a[1]*b[2]-b[1]*a[2],a[2]*b[0]-b[2]*a[0],a[0]*b[1]-b[0]*a[1]]
	return c
