"""
Insertion sort can be compared with playing cards :
That is, if you hold the first i – 1 cards in order, you pick the ith
card and compare it to these cards until its proper spot is found.

""" 

def insertionSort(arr):
  i = 1
  while i < len(arr):
    itemToInsert = arr[i]
    j = i - 1
    while j >= 0:
      if itemToInsert < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
      else:
        break
    arr[j+1] = itemToInsert
    i +=1 


arr = [64, 34, 25, 12, 22, 11, 90] 
  
insertionSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),
