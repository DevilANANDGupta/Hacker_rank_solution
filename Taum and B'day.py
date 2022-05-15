'''Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy  black gifts and  white gifts.

The cost of each black gift is  units.
The cost of every white gift is  units.
The cost to convert a black gift into white gift or vice versa is  units.
Determine the minimum cost of Diksha's gifts.

Example





He can buy a black gift for  and convert it to a white gift for , making the total cost of each white gift . That matches the cost of a white gift, so he can do that or just buy black gifts and white gifts. Either way, the overall cost is .

Function Description

Complete the function taumBday in the editor below. It should return the minimal cost of obtaining the desired gifts.

taumBday has the following parameter(s):

int b: the number of black gifts
int w: the number of white gifts
int bc: the cost of a black gift
int wc: the cost of a white gift
int z: the cost to convert one color gift to the other color
Returns

int: the minimum cost to purchase the gifts
Input Format

The first line will contain an integer , the number of test cases.

The next  pairs of lines are as follows:
- The first line contains the values of integers  and .
- The next line contains the values of integers , , and .

Constraints



Output Format

 lines, each containing an integer: the minimum amount of units Taum needs to spend on gifts.

Sample Input

STDIN   Function
-----   --------
5       t = 5
10 10   b = 10, w = 10
1 1 1   bc = 1, wc = 1, z = 1
5 9     b = 5, w = 5
2 3 4   bc = 2, wc = 3, z = 4
3 6     b = 3, w = 6
9 1 1   bc = 9, wc = 1, z = 1
7 7     b = 7, w = 7
4 2 1   bc = 4, wc = 2, z = 1
3 3     b = 3, w = 3
1 9 2   bc = 1, wc = 9, z = 2
Sample Output

20
37
12
35
12
Explanation

Test Case #01:
Since black gifts cost the same as white, there is no benefit to converting the gifts. Taum will have to buy each gift for 1 unit. The cost of buying all gifts will be: .

Test Case #02:
Again, he cannot decrease the cost of black or white gifts by converting colors.  is too high. He will buy gifts at their original prices, so the cost of buying all gifts will be: .

Test Case #03:
Since , he will buy  white gifts at their original price of .  of the gifts must be black, and the cost per conversion, . Total cost is .

Test Case #04:
Similarly, he will buy  white gifts at their original price, . For black gifts, he will first buy white ones and color them to black, so that their cost will be reduced to . So cost of buying all gifts will be: .

Test Case #05: He will buy black gifts at their original price, . For white gifts, he will first black gifts worth  unit and color them to white for  units. The cost for white gifts is reduced to  units. The cost of buying all gifts will be: .'''




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    # Write your code here
     return b * min(bc, wc + z) + w * min(wc, bc + z)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()



