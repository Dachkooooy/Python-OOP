# def possible_permutations(some_list:list):
#     if len(some_list) <= 1:
#         yield some_list
#     else:
#         for i in range(len(some_list)):
#             for perm in possible_permutations(some_list[:i] + some_list[i+1:]):
#                 yield [some_list[i]] + perm

import itertools

def possible_permutations(some_list: list):
    for perm in itertools.permutations(some_list):
        yield list(perm) # permutations returns tuples, that's why we cast to list

[print(n) for n in possible_permutations([1, 2, 3])]