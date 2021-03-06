## Python Generators

As Python 3 comes into maturity, generators are becoming more and more popular. In this post we are going to define what a generator is and does, breakdown a simple problem using a generator, and discuss some general use cases for generators.

### What is a generator?

To define a _generator_ we must first have a clear idea of _iterators_, _iterables_, and _iteration_ itself.

#### Iteration, Iterable, Iterator

*Iteration*: Accessing values in a set, one at a time and in order. 

*Iterable*: An object which contains a sequence of values. The `for` loop is an extremely common and useful way of accessing the values (ie _iterating over_ the values). As well in Python, the method `__iter__` can be used to return an _iterator_ to advance through the values as needed.
##### Iterables in Python:
* Strings
* Lists
* Tuples

*Iterator*: An [iterator](https://docs.python.org/3/tutorial/classes.html#iterators) is an object on which we can use the `__next__` method to access (in order) a value in a sequence. Iterators hold their state, ei keep track of where they are in the sequence. This is a very useful tool that allows a program to break up a loop into callable steps, offering more control and the ablitlty to share "loops" between functions.

#### Generator

[Generators](https://docs.python.org/3/tutorial/classes.html#generators) can be thought of as iterators that *create* values rather than access them. This is done by running the logic in the generator definition each time the `__next__` method is called with the generator object as its argument (ie `next(my_gen_obj)`). In other words, there is no list or tuple that stores all of the values that are to be looped over, they are created one by one as needed. The advantage of this approach is that nothing is stored. This has profound performance ramifications that can be of great advantage with large data sets.

If this isn't quite clear yet, no problem. In the next section we are going to get our hands dirty breaking down the syntax and use of a generator. Refer back to these definitions as you go through the rest of this post and try to connect the dots of the pieces you didn't quite understand.

### Solve Problems with Generators

#### Problem

* Create a generator `generate_seq()` that creates the infinite geometric series:
1, 1/2, 1/4, 1/8...
* Write a function `first_N(num)` that sums the first `num` values
* Write a function `until_small(epsilon)` that sums the sequence until the
next term is less than some small value `epsilon`.
* Write tests to drive the development proccess.

Lets write our tests first. Create a new directory called _python-generator_ and then add two files to that dir - _generator.py_ and _generator_tests.py_. Add the following code to _generator_tests.py_:

```python
import unittest
from generator import *

class SeqGenTest(unittest.TestCase):

    def test_first_N(self):
        self.assertEqual(first_N(0), 0.0) 
        self.assertEqual(first_N(1), 1.0) 
        self.assertEqual(first_N(2), 1.5) 
        self.assertEqual(first_N(3), 1.75) 
        self.assertEqual(first_N(4), 1.875) 

    def test_until_small(self):
        self.assertEqual(until_small(1.0 / 2), 1.5) 
        self.assertEqual(until_small(1.0 / 8), 1.875) 

if __name__ == '__main__':
    unittest.main()
``` 

With this block of code we have imported our testing module, `unittest`, which is included in the Python standard library. We also imported our functions (that we still need to define), from _generator.py_.

Running this code in our terminal produces this error:

```sh
EE
======================================================================
ERROR: test_first_N (__main__.SeqGenTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "generator_tests.py", line 7, in test_first_N
    self.assertEqual(first_N(0), 0.0)
NameError: name 'first_N' is not defined

======================================================================
ERROR: test_until_small (__main__.SeqGenTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "generator_tests.py", line 14, in test_until_small
    self.assertEqual(until_small(1.0 / 2), 1.5)
NameError: name 'until_small' is not defined

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (errors=2)
```

As would should expect, `first_N` and `until_small` are not defined. So lets do that now.

We need to create an infinite set of values, but we don't need these values all at one. Since we need an *infinite* set of values, we can't pre-define them in list or a tuple. Even if it was only 1 million values, we would not want to have to store all of these in memory because it would serioulsy bog down our machine. Again, we don't need these values all at once, so the best solution would be to create them one at a time, as we need them. How could we accomplish this? We could create a function that took our current value as an argument and returned the next value like so:

```python
def create_val(current_val):
  return current_val / 2
```

And that would work. But we would have to manually keep track of where we were in the sequence, which could get very cumbersome for any large set. In comes the *generator*, it does exactly what we need.

```python
def generate_seq():
    """Generates the infinite geometric series 1, 1/2, 1/4, 1/8, ..."""
    i = 1
    while True:
        yield 1.0 / i
        i *= 2
```

Now, this looks more or less like a typical Python function, but notice the `yield` key word. That is the heart of a generator definition. It is some what like a `return` statement, but does quite a bit more. When called, this `generate_seq()` will return a `<generator object>` that can easily be stored in a variable for use through out your program or function. Here is what that generator object does:

  * the code outside the of `while` block will only run once, when the generator is created
  * each `next()` call will run the the `while` loop one time
  * each `next()` call will return one value
  * after each `next()` call the generator will hold its newly changed state

Lets test this out. In the same file add this code:

> FYI: we are going to take this code out after we run it. It is only to make sure our generator works.

```python
gen = generate_seq()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
```
If you run that in your terminal:

```sh
$ python3 generator.py
```
You should see this: 

```sh
<generator object generate_seq at 0x101a0f728>
1.0
0.5
0.25
```

You can see that stored in the variable `gen` is in fact an object of type *generator*. As well, each next call produced a different value. Exactly what we wanted.

> Go ahead and take that previous bit of code out now, we no longer need it.

Lets now implement this generator in more dynamic ways by combining it with other functions. As stated in the original problem, we need to sum the first `num` values and we need to sum the values until the ouput of the generator is smaller than a specified value. Lets get to work. Before you read further, take a few stabs at solving this yourself. It will make the answers much more valuable to your learning proccess.

```python
def first_N(num):
    result = 0.0
    seq = generate_seq()
    for n in range(num):
        result += next(seq)
    return result
```
The breakdown: 
* We take an argument that tells us how many values to add together.
* Create a variable to hold our sum
* Instantiate a generator object and store in a variable
* Run a for loop and call the next method to create a new value in the sequence defined by our generator
* Keep a running sum of all of the values
* Return the total when the loop has executed `num` times  


```python
def until_small(epsilon):
    is_greater = True
    result = 0.0
    seq = generate_seq()
    while is_greater:
        current = next(seq)
        result += current
        is_greater = current > epsilon
    return result
```

The breakdown:
* Create a variable that we will use to eventually exit our `while` loop
* Create a variable to hold our sum
* Instantiate a generator object and store it in a variable
* Run a while loop that continues until `is_greater` is false
* Add the current value returned by the generator to our total
* Set `is_greater` to false when the value returned by the generator is less than epsilon, thus ending our loop
* Return the result

#### recap generators and use cases

