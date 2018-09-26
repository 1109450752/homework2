import math
x1,y1=eval(input(">>"))
x2,y2=eval(input(">>"))
#x1=39.55
#y1=-116.25
#x2=41.5
#y2=87.37
x1=math.radians(x1)
x2=math.radians(x2)
y1=math.radians(y1)
y2=math.radians(y2)
#print(x1,x2,y1,y2)
s=(math.sin(x1)*math.sin(x2))+(math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
s=6371.01*math.acos(s)
print(s)
