class Vector(list):
	def __init__(v,w=[]):
		if (w.__class__.__name__=="int"):
			v.__Calloc__(w)
		else:
			v.__Calloc__( len(w) )
			for i in range( len(w) ):
				v[i]=1.0*w[i]
        
	def __Calloc__(v,size):
		for i in range(size):
			v.append(0.0)
			
	def __add__(v,w):        
		u=Vector(v)
		for i in range(len(v)):
			u[i]+=w[i]
		return u
		
	def __sub__(v,w):
		u=Vector(v)
		for i in range(len(v)):
			u[i]-=w[i]
		return u
		
	def __mul__(v,arg2):
		if(arg2.__class__.__name__ == "Vector"):
			return v.__mul_Vector__(arg2)
		if(w.__class__.__name__=='int'):
			w*=1.0
		if(w.__class__.__name__=='float'):
			return v.__mul_Number__(arg2)
			
	def DotProduct(v,w):
		return v*w
	

v = Vector(5)
v = Vector([1,2,3,4])
w = Vector([1,2,3,4])
print(v+w)
