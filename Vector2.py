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
	
	def __add__(self, w):
		if(w.__class__.__name__!= 'Vector'):
			raise
		u = self		
		for i in range(len(u)):
			u[i] = w[i]+ u[i]
		return u
	def __repr__(self):
		return repr(self.v)
			 
a = Vector([5,3,4])
b = Vector([1,2,4])
print(a+b)
