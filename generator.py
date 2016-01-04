"""Create a generator gen_seq() that creates the infinite geometric series:
1, 1/2, 1/4, 1/8...

Write a function first_N(num) that sums the first num values

Write a function until_small(epsilon) that sums the sequence until the
additional term is less than some small value epsilon.

"""

def seq_generator():
    """Generates the infinite geometric series 1, 1/2, 1/4, 1/8, ..."""
    i = 1
    while True:
        yield 1.0 / i
        i *= 2

def first_N(num):
    """Use seq_generator() to generate the sum of the first num values of the series."""
    n = 0
    result = 0.0
    seq = seq_generator()
    while n < num:
        result += next(seq)
        n += 1
    return result

def until_small(epsilon):
    """Use seq_generator() to generate the sum of the series until a value smaller
    than epsilon is encountered."""
    current = 1
    result = 0.0
    seq = seq_generator()
    while current > epsilon:
        current = next(seq)
        result += current
    return result

