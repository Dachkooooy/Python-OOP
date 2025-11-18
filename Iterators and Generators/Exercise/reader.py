# Create a generator function called read_next() which should receive a different number of arguments (all iterable).
# On each iteration, the function should return each element from each sequence.
# Note: Submit only the function in the judge system
# Examples
# Test Code	Output
# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')	string2dict


def read_next(*args):
    for iterable in args:
        # for item in iterable:
        #     yield item
        yield from iterable

# Test Code
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
        