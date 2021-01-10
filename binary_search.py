#Binary Search
def binary_search(arr, target):
      lo = 0
      hi = len(arr) -1
      while lo <= hi:
          mid = (lo + hi)//2
          
          if target < arr[mid]:
              hi = mid - 1
          elif target > arr[mid]:
              lo = mid + 1
          else:
              return True
          
        # Element is not present in the array 
      return -1


# Test array 
arr = [ 2, 3, 4, 10, 40, 7 ] 
target = 10
  
# Function call 
result = binary_search(arr, target) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 