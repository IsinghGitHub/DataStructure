# Data-Structure

# **Binary Array Search**

Binary Array Search is a fundamental algorithm in computer science because of its time complexity. Let’s first review a Python implementation below that searches for `target` in an ordered list, `A`.

![https://learning.oreilly.com/library/view/learning-algorithms/9781492091059/assets/bas.jpg](https://learning.oreilly.com/library/view/learning-algorithms/9781492091059/assets/bas.jpg)

### *Figure 2-6. Annotated Binary Array Search*

Initially `lo` and `hi` are set to the leftmost and rightmost indices of `A`. While there is a sublist to explore, find the midpoint, `mid`, using integer division. If `A[mid]` is `target` your search is over; otherwise you have learned whether to search the sublist to the left, `A[lo .. mid-1]`, or to the right, `A[mid+1 .. hi]`.

This algorithm determines whether a value exists in a sorted list of N elements. As the loop iterates, eventually either the `target` will be found or `hi` crosses over to become smaller than `lo`, which ends the loop.
