num = int(input())
k = int(input())
# we need to make a mask which is 31 left shifted by k
mask = 31 << k
bit = num & mask
print(bin(bit))