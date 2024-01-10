def bubbleSort(arr):
    n = len(arr)
    didSwap = 0
    for i in range(n-1,-1,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                didSwap = 1
        if didSwap == 0:
            break

arr = list(map(int,input().split()))
bubbleSort(arr)
print(arr)