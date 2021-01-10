## SelectionSort

```python
# Python program for implementing BubbleSort

def SelectionSort(arr):
	n = len(arr)

# Traverse through all the array elements
for i in range(n):
	# Find the minimum element in remaining unsorted array

	min_idx = i
	for j in range(i+1, n):
			# traverse the array from 0 to len of array
			
			if arr[min_idx] > arr[j]:
					min_idx = j
			# Swap the found min_element with the first element
			a[j],a[min_idx] = a[min_idx],a[j]
	return arr

```

Let's see how it works in action with a list that contains the following elements: `[3, 5, 1, 2, 4]`.

We begin with the unsorted list:

- 3 5 1 2 4

The unsorted section has all the elements. We look through each item and determine that `1` is the smallest element. So, we swap `1` with `3`:

- **1** 5 3 2 4

Of the remaining unsorted elements, `[5, 3, 2, 4]`, `2` is the lowest number. We now swap `2` with `5`:

- **1 2** 3 5 4

This process continues until the list is sorted:

- **1 2 3** 5 4
- **1 2 3 4** 5
- **1 2 3 4 5**

Let's see how we can implement this in Python!

```python
def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)-1):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]
```

```python
L = [3, 1, 41, 59, 26, 53, 59]
print(L)
selection_sort(L)

# Let's see the list after we run the Selection Sort
print(L)
```

### **Time Complexity Calculation**

So how long does it take for selection sort to sort our list? We are going to take an approach and calculate exactly how much time the selection sort algorithm takes, given an array of size `n`. The first line of the code is:

```
def selection_sort(L):

```

This line shouldn't take that much since it's only setting the function stack. We say that this is a *constant* - the size of our input does not change how long it takes for this code to run. Let's say it takes `c1` operations to perform this line of code. Next, we have:

```
for i in range(len(L)-1):

```

This one is a little trickier. 

First of all, we have two function invocations, `len()` and `range()`, which are performed before the `for` loop begins. The cost of `len()` is also independent of size in CPython, which is the default Python implementation on Windows, Linux, and Mac.

 This is also true for the initialization of `range()`. Let's call these two together `c2`.

Next, we have the `for`, which is running `n - 1` times. This is not a constant, the size of the input does make an impact on how long this is executed. So we have to multiply whatever time it takes for one loop to complete by `n - 1`.

There is a constant cost for evaluating the `in` operator, let's say `c3`. That covers the outer for-loop.

The variable assignment is also done in constant time. We'll call this one `c4`:

```
min_index = i

```

We now encounter the inner for-loop. It has two constant function invocations. Let's say they take `c5` operations.

> Note that c5 is different from c2, because range here has two arguments, and there is an addition operation being performed here.

So far we have `c1 + c2 + (n - 1) * (c3 + c4 + c5)` operations, and then our inner loop begins, multiplying everything by...? Well, it's tricky, but if you look closely, it takes `n - 2` times in the first loop, `n - 3` in the second one, and 1 in the last time.

We need to multiply everything by the sum of all numbers between 1 and `n - 2`. Mathematicians have told us that the sum would be `(n - 2) * (n - 1) / 2`. Feel free to read more about the sum of integers between 1 and any positive number `x` [here](https://www.wikihow.com/Sum-the-Integers-from-1-to-N).

The contents of the inner loop are completed in constant time as well. Let's assign the time it takes Python to do the `in`, `if`, assignment statement and the variable swap take up an arbitrary constant time of `c6`.

```
for j in range(i+1, len(L)-1):
    if L[j] < L[min_index]:
        min_index = j
L[i], L[min_index] = L[min_index], L[i]

```

All-together we get `c1 + c2 + (n - 1) * (c3 + c4 + c5) + (n - 2) * (n - 3) * c6 / 2`.

We can simplify this to: `a * n * n + b * n + c`, where `a`, `b` and `c` representing the values of the evaluated constants.

This is known as *O(n^2)*. What does that mean? In summary, our algorithm's performance is based on the squared size of our input list. Therefore, if we double the size of our list, the time it takes to sort it would be multiplied by 4! If we divide the size of our input by 3, the time would shrink by 9!