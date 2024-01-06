import math
x,y = map(int,input().split())
nextPowerOfTwo = math.ceil(math.log2(x+1))
p = 1 << nextPowerOfTwo
print(p,p-1)