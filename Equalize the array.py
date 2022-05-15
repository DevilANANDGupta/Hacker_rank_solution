'''Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.

Example


Delete the  elements  and  leaving . If both twos plus either the  or the  are deleted, it takes  deletions to leave either  or . The minimum number of deletions is .

Function Description

Complete the equalizeArray function in the editor below.

equalizeArray has the following parameter(s):

int arr[n]: an array of integers
Returns

int: the minimum number of deletions required
Input Format

The first line contains an integer , the number of elements in .
The next line contains  space-separated integers .

Constraints

Sample Input

STDIN       Function
-----       --------
5           arr[] size n = 5
3 3 2 1 3   arr = [3, 3, 2, 1, 3]
Sample Output

2   
Explanation

Delete  and  to leave . This is minimal. The 
only other options are to delete  elements to get an array of either  or .'''






#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    return(len(arr)- arr.count(max(set(arr), key = arr.count )))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
