k=0
l=0
input=open('input.txt','r')
output=open('output.txt','w')
b=input.readline().split()
n=int(b[0])
k=int(b[1])
d=[0]*n
for i in range(k):
    a=input.readline().split()
    d[int(a[0])-1]-=int(a[2])
    d[int(a[1])-1]+=int(a[2])
for i in range(n):
    print(d[i],end=' ',file=output)
