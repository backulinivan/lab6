k=0
l=0
input=open('input.txt','r')
output=open('output.txt','w')
n=int(input.readline())
a=input.readline().split()
for i in range(n):
  a[i]=int(a[i])
min=n+1
for i in range(n):
  if((a[i])<0)and(a[i+1:].count(-a[i])>0):

    k=a.index(-a[i])-i
    if k<min:
      min=k
if min==n+1:
  print(0, file=output)
else:
  print(min, file=output)
