'''We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range .

Example

$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

The matrix looks like this:

5 3 4
1 5 8
6 4 2
We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2
This took three replacements at a cost of .

Function Description

Complete the formingMagicSquare function in the editor below.

formingMagicSquare has the following parameter(s):

int s[3][3]: a  array of integers
Returns

int: the minimal total cost of converting the input square to a magic square
Input Format

Each of the  lines contains three space-separated integers of row .

Constraints

Sample Input 0

4 9 2
3 5 7
8 1 5
Sample Output 0

1
Explanation 0

If we change the bottom right value, , from  to  at a cost of ,  becomes a magic square at the minimum possible cost.

Sample Input 1

4 8 2
4 5 7
6 1 6
Sample Output 1

4
Explanation 1

Using 0-based indexing, if we make

-> at a cost of 
-> at a cost of 
-> at a cost of ,
then the total cost will be .'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]


def formingMagicSquare(s):
    # Write your code here
    results = []
    for p in pre:
        total = 0
        for p_row, s_row in zip(p, s):
            for i, j in zip(p_row, s_row):
                if not i == j:
                    total += max([i, j]) - min([i, j])
            
        results.append(total)
        
    return min(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()


