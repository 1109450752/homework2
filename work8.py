import os
f=open("/tmp/yy.txt")
q=f.read()
s=''
for i in str(q):
   # print(ord(i)+2,end="")
    s=s+str(ord(i)+2)
#print()
#print(s)
s1=open("/tmp/yy1.txt",'w')
s1.write(s)
s1.close()
#print(q)
