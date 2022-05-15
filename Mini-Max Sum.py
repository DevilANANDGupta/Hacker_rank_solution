'''Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24 . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of 5 integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of 4  of 5 elements.

Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

Sum everything except , the sum is 2+3+4+5=14.
Sum everything except , the sum is 1+3+4+5=13 .
Sum everything except , the sum is 1+2+4+5=12 .
Sum everything except , the sum is  1+2+4+5=11
Sum everything except , the sum is 1+2+4+5=10 .
Hints: Beware of integer overflow! Use 64-bit Integer.

Need help to get started? Try the Solve Me First problem'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    hold = [None]*int(len(arr)-3)
    for i in range (0,len(arr)-3):
        temp =0 
        for j in range(i,i+4):
            temp = temp+arr[j]
        hold[i] = temp
    print(hold[0],hold[-1])    
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


