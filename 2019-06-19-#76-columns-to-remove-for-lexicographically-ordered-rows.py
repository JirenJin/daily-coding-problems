"""
You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.
"""


def num_of_columns_to_remove(matrix):
    def is_sorted(array):
        maximum = chr(ord('a') - 1)
        for ch in array:
            if ch <= maximum:
                return False
            maximum = max(maximum, ch)
        return True
    count = 0
    for column in zip(*matrix):
        if not is_sorted(column):
            count += 1
    return count


if __name__ == "__main__":
    test_cases = [['c','b','a'], ['d','a','f'], ['g','h','i']]
    test_cases = [['a', 'b', 'd', 'e'], ['c', 'z', 'a', 'f']]
    print(num_of_columns_to_remove(test_cases[:]))
