inputA = open('inputA.txt', 'r')
outputA = open('outputA.txt', 'w')

num = int(inputA.readline())
numArr = list(map(int, inputA.readline().split()))
for i in range(num):
    if numArr.count(numArr[i]) == 2:
        reqNum = numArr[i]
outputA.write(str(reqNum))        
