# Data-Structure

# **Binary Array Search**

Binary Array Search is a fundamental algorithm in computer science because of its time complexity. Let’s first review a Python implementation below that searches for `target` in an ordered list, `A`.

![https://learning.oreilly.com/library/view/learning-algorithms/9781492091059/assets/bas.jpg](https://learning.oreilly.com/library/view/learning-algorithms/9781492091059/assets/bas.jpg)

### *Figure 2-6. Annotated Binary Array Search*

Initially `lo` and `hi` are set to the leftmost and rightmost indices of `A`. While there is a sublist to explore, find the midpoint, `mid`, using integer division. If `A[mid]` is `target` your search is over; otherwise you have learned whether to search the sublist to the left, `A[lo .. mid-1]`, or to the right, `A[mid+1 .. hi]`.

This algorithm determines whether a value exists in a sorted list of N elements. As the loop iterates, eventually either the `target` will be found or `hi` crosses over to become smaller than `lo`, which ends the loop.


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