from math import *
from Vector import *
class Canvas:
	P1=None
	P2=None 
	R=None
	A=[0.0,0.0]
	B=[0.0,0.0]
	def __init__(self,r,p1,p2):
		self.R=r
		self.P1=p1
		self.P2=p2
		self.Initialize()
	#Initialize Parameters A,B from R,P1 and P2
	def Initialize(self):
		self.A[0]=(1.0*( self.P2[0]-self.P1[0] ))/(1.0*(self.R[0] ))
		self.A[1]=(1.0*( self.P1[1]-self.P2[1] ))/(1.0*(self.R[1] ))
		self.B[0]=-self.A[0]*self.P1[0]
		self.B[1]=-self.A[1]*self.P2[1]
	#Convert geometric point to pixels.
	def Point_2_Pixels(self,p):
		px=[0,0]
		for i in range(2):
			px[i]=self.A[i]*p[i]+self.B[i]
		return px 
	#Convert geometric points to pixels. 
	def Points_2_Pixels(self,ps):
		pxs=[]
		for p in ps:
			pxs.append( self.Point_2_Pixels(p) )
		return pxs
class Curve:
	t1=0.0
	t2=2.0*pi
	N = 360
	def __init__(self):
		return
	def r(self,t):
		return Vector([cos(t) , sin(t)])
	def rs(self):
		t = self.t1
		dt = (self.t2-self.t1)/(1.0*self.N)
		self.Rs = []
		for i in range(self.N+1):
			r = self.r(t)
			self.Rs.append(r)
			t +=dt
		return  self.Rs

curve = Curve()
print curve.rs()	

#p1=[-1.0,-1.0]
#p2=[1.0,1.0]
#R=[100,100]
#canvas = Canvas(R,p1,p2)
#print canvas
#print 1,canvas.Point_2_Pixel(p1)
#print 2,canvas.Point_2_Pixel(p2)
