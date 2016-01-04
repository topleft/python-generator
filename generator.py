"""Create a generator gen_seq() that creates the infinite geometric series:
1, 1/2, 1/4, 1/8...

Write a function first_N(num) that sums the first num values

Write a function until_small(epsilon) that sums the sequence until the
additional term is less than some small value epsilon.

"""

def generate_seq():
    """Generates the infinite geometric series 1, 1/2, 1/4, 1/8, ..."""
    i = 1
    while True:
        yield 1.0 / i
        i *= 2

def first_N(num):
    """Use generate_seq() to generate the sum of the first num values of the series."""
    result = 0.0
    seq = generate_seq()
    for n in range(num):
        result += next(seq)
    return result

def until_small(epsilon):
    """Use generate_seq() to generate the sum of the series until a value smaller
    than epsilon is encountered."""
    is_greater = True
    result = 0.0
    seq = generate_seq()
    while is_greater:
        current = next(seq)
        result += current
        is_greater = current > epsilon
    return result


gen = generate_seq()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

