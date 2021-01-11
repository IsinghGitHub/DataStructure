![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5b1abd1f-1edd-4281-8798-d89e041f0357/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5b1abd1f-1edd-4281-8798-d89e041f0357/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f10360e-27a3-4386-af9e-9c0b9c22c383/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f10360e-27a3-4386-af9e-9c0b9c22c383/Untitled.png)

# Measuring the Complexity of Algorithms

We can use computers clock to measure the run time of an algorithm. This process is known is benchmarking or profiling.

```python
"""
File: timing1.py
Prints the running times for problem sizes that double,
using a single loop.
"""
import time
problemSize = 10000000
print("%12s%16s" % ("Problem Size", "Seconds"))

for count in range(5):
    start = time.time()
    # The start of the algorithm
    work = 1
    for x in range(problemSize):
      work += 1
      work -= 1
# The end of the algorithm
elapsed = time.time() - start
print("%12d%16.3f" % (problemSize, elapsed))
problemSize *= 2
```

The test run of the code above shows the below results:

```python
indrajitsingh@isingh Data Structure % python3 time_complexity.py
Problem Size         Seconds
     1000000           0.120
indrajitsingh@isingh Data Structure % python3 time_complexity.py
Problem Size         Seconds
    10000000           1.225
indrajitsingh@isingh Data Structure % python3 time_complexity.py
Problem Size         Seconds
   100000000          13.651
indrajitsingh@isingh Data Structure % python3 time_complexity.py
Problem Size         Seconds
   160000000          19.167
```

This indicates as the problem size increases the time taken to run the programme increases.

Let's check another version of the programme using two for loops:

In this version, the extended assignments have been moved into a nested loop. This
loop iterates through the size of the problem within another loop that also iterates
through the size of the problem.

```python
"""
File: time_complexity.py
Prints the running times for problem sizes that double,
using a single loop.
"""
import time
problemSize = 16000
print("%12s%16s" % ("Problem Size", "Seconds"))

for count in range(5):
    start = time.time()
    # The start of the algorithm
    work = 1
    for j in range(problemSize):
      for k in range(problemSize):
        work += 1
        work -= 1
# The end of the algorithm
elapsed = time.time() - start
print("%12d%16.3f" % (problemSize, elapsed))
problemSize *= 2
```

If we add one more loop , the calculation time increases further and it goes exponentially higher based on the problem size.

The major problems with this technique are:

1. Different Hardware platforms have different processing speeds.
2. The running time of a algorithms varies based on the operating system it runs.
3. It is impractical to run very large dataset to test an algorithm efficiency.

## Orders of Complexity

Let's discuss the two problems discussed earlier.

The first loop executes n times for a
problem of size n. The second loop contains a nested loop that iterates

$n^2$ times.

Very interestingly , the amount of work done by these two algorithms is similar for small values of n but is very different for large values of n.

Check the image below



The performance of the first algorithm is linear in that its work grows in direct proportion to the size of the problem (problem size of 10, work of 10; 20 and 20; and so on). 

The behavior of the second algorithm is quadratic in that its work grows as a function of the square of the problem size (problem size of 10, work of 100).

Although $n^2$ is worse in some sense than $n^2$, they are both of the polynomial order and
are better than the next higher order of complexity. 

An order of complexity that is worse than polynomial is called exponential. An example rate of growth of this order is $n^2$

Exponential algorithms are impractical to run with large problem sizes.

