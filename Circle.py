from math import *
from Curve import Curve from Vector import Vector class Circle(Curve): C=Vector([0.0,0.0]) r=1.0 def R(self,t): return Vector([ self.C[0]+self.r*cos(t), self.C[1]+self.r*sin(t) ]) def PMin(self): return Vector([-self.r,-self.r]) def PMax(self): return Vector([self.r,self.r]) curve=Circle() curve.Rs() print curve.Pxs()
