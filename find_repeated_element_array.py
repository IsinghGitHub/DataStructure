#User function Template for python3

def repeat_func(arr):
    repeated = []
    track = []
    size = len(arr)
    for i in range(size):
        k = i + 1
        count = 0
        for j in range(k,size):
            if (arr[i] == arr[j] and arr[i] not in repeated):
                repeated.append(arr[i])

            
    return repeated
    
arr  = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(repeat_func(arr))