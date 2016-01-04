## Python Generators

As Python 3 comes into maturity, generators are becoming more and more popular. In this post we are going to define what a generator is and does, breakdown a simple problem using a generator, and discuss some general use cases for generators.

#### What is a generator?

To define a _generator_ we must first have a clear idea of _iterators_, _iterables_, and _iteration_ itself.

##### Iteration, Iterable, Iterator

> Iteration: Accessing values in a set, one at a time and in order. 

> Iterable: An object which contains a sequence of values. The `for` loop is an extremely common and useful way of accessing the values (ie _iterating over_ the values). As well in Python, the method `__iter__` can be used to return an _iterator_ to advance through the values as needed.
> #### Iterables in Python:
> * Strings
> * Lists
> * Tuples

> [Iterator](https://docs.python.org/3/tutorial/classes.html#iterators): An object on which we can use the `__next__` method to access (in order) a value in a sequence. Iterators hold their state, ei keep track of where they are in the sequence. This is a very useful tool that allows a program to break up a loop into callable steps, offering more control and the ablitlty to share "loops" between functions.

##### Generator

[Generators](https://docs.python.org/3/tutorial/classes.html#generators) can be thought of as iterators that *create* values rather than access them. This is done by running the logic in the generator definition each time the `__next__` method is called with the generator object as its argument (ie `next(my_gen_obj)`). In other words, there is no list or tuple that stores all of the values that are to be looped over, they are created one by one as needed. The advantage of this approach is that nothing is stored. This has profound performance ramifications that can be of great advantage with large data sets.

If this isn't quite clicking for you, no problem. In the next section we are going to get our hands dirty breaking down the syntax and use of a generator. Refer back to these definitions as you go through the rest of this post and try to connect the dots of the pieces you didn't quite understand.


#### define the problem and introduce functions that we will use to solve it

#### pip install pytest?

#### show test code

#### show first error

#### show first solution

#### continue until solution is complete

#### recap generators and use cases