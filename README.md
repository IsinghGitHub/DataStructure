# Data-Structure

# What is a Data Structure:

A data structure (DS) is a way of organizing data so that it can be used effectively.

# Why Data Structure:

They are an essential ingerdient in creating fast and powerful algorithms. Also Data Structures help in organizing the data. They make the code cleaner and better organized.

# What is an Abstract Data Type:

An Abstract Data Type (ADT) is and abstraction of data structure which provides only the interface to which a
data structure must adhere to.

The interface doesn't give any specific details about how something should be implemented or in what programming language.

[List](https://en.wikipedia.org/wiki/List_of_data_structures)

[Queue](<https://en.wikipedia.org/wiki/Queue_(abstract_data_type)>)

[Map ](https://en.wikipedia.org/wiki/Associative_array)

[Vehicle]()

[](https://www.notion.so/f3db7fd377fc41a3b4af8bb03622938d)

# **Binary Array Search**

Binary Array Search is a fundamental algorithm in computer science because of its time complexity. Let’s first review a Python implementation below that searches for `target` in an ordered list, `A`.

![https://learning.oreilly.com/library/view/learning-algorithms/9781492091059/assets/bas.jpg](https://learning.oreilly.com/library/view/learning-algorithms/9781492091059/assets/bas.jpg)

### _Figure 2-6. Annotated Binary Array Search_

Initially `lo` and `hi` are set to the leftmost and rightmost indices of `A`. While there is a sublist to explore, find the midpoint, `mid`, using integer division. If `A[mid]` is `target` your search is over; otherwise you have learned whether to search the sublist to the left, `A[lo .. mid-1]`, or to the right, `A[mid+1 .. hi]`.

This algorithm determines whether a value exists in a sorted list of N elements. As the loop iterates, eventually either the `target` will be found or `hi` crosses over to become smaller than `lo`, which ends the loop.

### Time Complexity of BinarySearch

The total time complexity of the above algorithm is O(log(n)), where n is the total number of elements in the array.

For `BinaryArraySearch`, the **while** loop iterates no more than `floor`(`log2` (N)) + `1` times. This behavior is truly extraordinary! With one million elements in sorted order, you can locate any element in just `21` passes through the **while** loop.

### Some applications are:

When you search for a name of the song in a sorted list of songs, it performs binary search and string-matching to quickly return the results.
Used to debug in git through git bisect

## Bubble Short

### Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

## **Steps for performing a Bubble Sort**

- Compare first and second element in the list and swap if they are in the wrong order.
- Compare second and third element and swap them if they are in the wrong order.
- Proceed similarly until the last element of the list in a similar fashion.
- Keep repeating all of the above steps until the list is sorted.

## Complexity Analysis of Bubble Sort

In Bubble Sort, **n-1** comparisons will be done in the 1st pass, **n-2** in 2nd pass, **n-3** in 3rd pass and so on. So the total number of comparisons will be,

```python
(n-1) + (n-2) + (n-3) + ..... + 3 + 2 + 1
Sum = n(n-1)/2
i.e O(n2)
```

Hence the **time complexity** of Bubble Sort is **O(n^2)**.

The main advantage of Bubble Sort is the simplicity of the algorithm.

The **space complexity** for Bubble Sort is **O(1)**, because only a single additional memory space is required i.e. for `temp` variable.

Also, the **best case time complexity** will be **O(n)**, it is when the list is already sorted.

Following are the Time and Space complexity for the Bubble Sort algorithm.

- Worst Case Time Complexity [ Big-O ]: **O(n2)**
- Best Case Time Complexity [Big-omega]: **O(n)**
- Average Time Complexity [Big-theta]: **O(n2)**
- Space Complexity: **O(1)**

## InsertionSort

**Time Complexity:**

In worst case, each element is compared with all the other elements in the sorted array. For N

elements, there will be $N^2$ comparisons. Therefore, the time complexity is O(N^2)

### **Quicksort**

The basic version of the algorithm does the following:

- Divide the collection in two (roughly) equal parts by taking a pseudo-random element and using it as a pivot.
- Elements smaller than the pivot get moved to the left of the pivot, and elements larger than the pivot to the right of it.
- This process is repeated for the collection to the left of the pivot, as well as for the array of elements to the right of the pivot until the whole array is sorted.

Quicksort will, more often than not, fail to divide the array into equal parts. This is because the whole process depends on how we choose the pivot.

We need to choose a pivot so that it's roughly larger than half of the elements, and therefore roughly smaller than the other half of the elements. As intuitive as this process may seem, it's very hard to do.

The most straight-forward approach is to simply choose the first (or last) element. This leads to Quicksort, ironically, performing very badly on already sorted (or almost sorted) arrays.

This is how most people choose to implement Quicksort and, since it's simple and this way of choosing the pivot is a very efficient operation (and we'll need to do it repeatedly), this is exactly what we will do.

## Implementation

Let's go through how a few recursive calls would look:

- When we first call the algorithm, we consider all of the elements - from indexes *0* to *n-1* where *n* is the number of elements in our array.
- If our pivot ended up in position *k*, we'd then repeat the process for elements from *0* to *k-1* and from *k+1* to *n-1*.
- While sorting the elements from *k+1* to *n-1*, the current pivot would end up in some position *p*. We'd then sort the elements from *k+1* to *p-1* and *p+1* to *n-1*, and so on.

That being said, we'll utilize two functions - `partition()` and `quick_sort()`. The `quick_sort()` function will first `partition()` the collection and then recursively call itself on the divided parts.

Let's start off with the `partition()` function:

# Binary Search Trees

A tree is a undirected graph which satifies any of the following definitions:

- An Acyclic connected graph

- A connected graph with N nodes and N-1 edges

- An graph in which any two vertices are connected by exactly one path

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bab69401-e980-43c0-aa18-b6618b71e695/binaryTreeSimple.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bab69401-e980-43c0-aa18-b6618b71e695/binaryTreeSimple.png)
