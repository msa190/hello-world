class SVG:
	Header=[
		'<?xml version="1.0"?>', '<?xml-stylesheet type="text/css" href="http://127.0.0.1/poops.css" ?>',
		'<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"', '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">',
		'<svg height="800" version="1.1" viewBox="0 0 800 800" width="800"',
		'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">',
	]
	Tail=['</svg>'] 
	def Line(self,px1,px2):
		return "<line x1='"+str(px1[0])+"' y1='"+str(px1[1])+"' x2='"+str(px2[0])+"' y2='	"+str(px2[1])+"'/>"
		
svg=SVG()
print svg.Line([10,20],[30,40]) 
