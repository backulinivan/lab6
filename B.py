k=0
l=0
input=open('input.txt','r')
output=open('output.txt','w')
n=int(input.readline())
a=input.readline().split()
for i in range(n):
    kupura=int(a[i])
    kupura=(kupura-5)//5
    if kupura==0:
        k-=1
    elif kupura<(-k):
        k+=kupura
    else:
        l+=k+kupura
        k=0
print(l,file=output)
