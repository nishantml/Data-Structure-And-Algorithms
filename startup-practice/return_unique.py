"""

In each input list, every number repeats at least once, except for two. Write a function that returns the two unique numbers.

Examples
return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
Notes
Keep the same ordering in the output.

"""


def return_unique(lst):
    uniqueLst = []
    for i in range(len(lst)):
        val = lst.pop(i)
        if val not in lst:
            uniqueLst.append(val)
        lst.insert(i, val)

    return uniqueLst


print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
