def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini],arr[i] = arr[i],arr[mini]
        
arr = list(map(int,input().split()))
selectionSort(arr)
print(arr)