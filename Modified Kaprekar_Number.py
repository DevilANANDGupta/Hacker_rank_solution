'''A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers, you have the same value you started with.

Consider a positive whole number  with  digits. We square  to arrive at a number that is either  digits long or  digits long. Split the string representation of the square into two parts,  and . The right hand part,  must be  digits long. The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get .

Example



First calculate that . Split that into two strings and convert them back to integers  and . Test , so this is not a modified Kaprekar number. If , still , and . This gives us , the original .

Note: r may have leading zeros.

Here's an explanation from Wikipedia about the ORIGINAL Kaprekar Number (spot the difference!):

In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.

Given two positive integers  and  where  is lower than , write a program to print the modified Kaprekar numbers in the range between  and , inclusive. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE.

Function Description

Complete the kaprekarNumbers function in the editor below.

kaprekarNumbers has the following parameter(s):

int p: the lower limit
int q: the upper limit
Prints

It should print the list of modified Kaprekar numbers, space-separated on one line and in ascending order. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE. No return value is required.

Input Format

The first line contains the lower integer limit .
The second line contains the upper integer limit .

Note: Your range should be inclusive of the limits.

Constraints


Sample Input

STDIN   Function
-----   --------
1       p = 1
100     q = 100
Sample Output

1 9 45 55 99

Explanation

, , , , and  are the modified Kaprekar Numbers in the given range.'''



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#
def is_kaprekar(num):
    if num < 4:
        if num == 1:
            return True
        else:
            return False
    num_sq = pow(num, 2)
    num_sq_str = str(num_sq)
    
    left = num_sq_str[:len(num_sq_str)//2]
    right = num_sq_str[len(num_sq_str)//2:]
    
    #print("left = {} right = {}".format(left, right))
    
    if int(left) + int(right) == num:
        return True
    else:
        return False

def kaprekarNumbers(p, q):
    # Write your code here
    out = []
    for num in range(p, q + 1):
        if is_kaprekar(num):
            out.append(num)
    return out

if __name__ == "__main__":
    p = int(input().strip())
    q = int(input().strip())
    result = kaprekarNumbers(p, q)
    if result:
        print (" ".join(map(str, result)))
    else:
        print("INVALID RANGE")



