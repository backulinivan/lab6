input=open('input.txt','r')
output=open('output.txt','w')
n=int(input.readline().rstrip())
f=True
i=1
a = list(map(int,input.readline().split()))
a=sorted(a)
while f:
    print(i,a[i-1],a[i])
    if a[i]==a[i-1]:
        f=False
        print(a[i],file=output)
    i+=1

