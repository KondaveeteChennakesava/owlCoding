num = int(input())
k = int(input())
# we need to make a mask which is 1 left shifted by k
mask = 1 << k
bit = num & mask
print(bin(mask))
if bit:
    print(1)
else:
    print(0)