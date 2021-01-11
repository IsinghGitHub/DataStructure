
def swap(lyst, i, j):
  
  """Exchanges the items at positions i and j."""
# You could say lyst[i], lyst[j] = lyst[j], lyst[i]
# but the following code shows what is really going on
  temp = lyst[i]
  lyst[i] = lyst[j]
  lyst[j] = temp


def bubbleSortWithTweak(arr):
  
  n = len(arr)
  
  while n > 1:
  
    swapped = False
    i=1
    while i < n:
      if arr[i] < arr[i - 1]: # Exchange if needed
        swap(arr, i, i - 1)
        swapped = True
      i += 1
    if not swapped: return # Return if no swaps
    n -= 1


arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSortWithTweak(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),
