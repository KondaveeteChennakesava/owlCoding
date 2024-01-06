import math
def printBinary(n):
    for i in range(31,-1,-1):
        if n & (1<<i):
            print(1,end='')
        else:
            print(0,end='')
    print()

def MSB(n):
    for i in range(31,-1,-1):
        if n & (1<<i):
            print(i)
            break
def LSB(n):
    for i in range(0,32,1):
        if n & (1<<i):
            print(i)
            break
# def clz(n):
#     print(n.bit_length() - len(bin(n).lstrip('-0b')))

n = int(input())

printBinary(n)
MSB(n)
LSB(n)
# clz(n) #No of leading zeros

nextPowerOfTwo = math.ceil(math.log2(n))
print(nextPowerOfTwo)

prevPowerOfTwo = math.ceil(math.sqrt(1 << (nextPowerOfTwo - 1)))
print(prevPowerOfTwo)

print(n.bit_count)