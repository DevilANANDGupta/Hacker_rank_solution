'''There are a number of people who will be attending ACM-ICPC World Finals. Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, presented as binary strings, determine the maximum number of topics a 2-person team can know. Each subject has a column in the binary string, and a '1' means the subject is known while '0' means it is not. Also determine the number of teams that know the maximum number of topics. Return an integer array with two elements. The first is the maximum number of topics known, and the second is the number of teams that know that number of topics.

Example



The attendee data is aligned for clarity below:

10101
11110
00010
These are all possible teams that can be formed:

Members Subjects
(1,2)   [1,2,3,4,5]
(1,3)   [1,3,4,5]
(2,3)   [1,2,3,4]
In this case, the first team will know all 5 subjects. They are the only team that can be created that knows that many subjects, so  is returned.

Function Description

Complete the acmTeam function in the editor below.
acmTeam has the following parameter(s):

string topic: a string of binary digits
Returns

int[2]: the maximum topics and the number of teams that know that many topics
Input Format

The first line contains two space-separated integers  and , where  is the number of attendees and  is the number of topics.

Each of the next  lines contains a binary string of length .

Constraints



Sample Input

4 5
10101
11100
11010
00101
Sample Output

5
2
Explanation

Calculating topics known for all permutations of 2 attendees we get:







The 2 teams (1, 3) and (3, 4) know all 5 topics which is maximal.'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    most = 0
    most_cnt = 0
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            x = sum(t1 == "1" or t2 == "1" for t1, t2 in zip(topic[i], topic[j]))
            if x > most:
                most = x
                most_cnt = 1
            elif x == most:
                most_cnt += 1
    return most, most_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


