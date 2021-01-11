def Selection_Sort(arr):
  n = len(arr)
  for i in range(n-1):

    min_idx = i

    for j in range(i+1,n):
      if arr[j] > arr[min_idx]:
        j = min_idx
      arr[j],arr[min_idx] = arr[min_idx],arr[j]
  return arr

arr = [7,18,1,3,89,8]
result = Selection_Sort(arr)
print(result)