#User function Template for python3

def largest( arr,n):
    l = len(arr)
    max = arr[0]
    for i in range(1,l):
             if  arr[i] > max:
                max = arr[i]
    return max

arr = [7,18,1,3,89,8]
n = 5
print(largest( arr,n))