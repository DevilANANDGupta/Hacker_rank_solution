'''You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.

A queen is standing on an  chessboard. The chess board's rows are numbered from  to , going from bottom to top. Its columns are numbered from  to , going from left to right. Each square is referenced by a tuple, , describing the row, , and column, , where the square is located.

The queen is standing at position . In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from :

image

There are obstacles on the chessboard, each preventing the queen from attacking any square beyond it on that path. For example, an obstacle at location  in the diagram above prevents the queen from attacking cells , , and :

image

Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at . In the board above, there are  such squares.

Function Description

Complete the queensAttack function in the editor below.

queensAttack has the following parameters:
- int n: the number of rows and columns in the board
- nt k: the number of obstacles on the board
- int r_q: the row number of the queen's position
- int c_q: the column number of the queen's position
- int obstacles[k][2]: each element is an array of  integers, the row and column of an obstacle

Returns
- int: the number of squares the queen can attack

Input Format

The first line contains two space-separated integers  and , the length of the board's sides and the number of obstacles.
The next line contains two space-separated integers  and , the queen's row and column position.
Each of the next  lines contains two space-separated integers  and , the row and column position of .

Constraints

A single cell may contain more than one obstacle.
There will never be an obstacle at the position where the queen is located.
Subtasks

For  of the maximum score:

For  of the maximum score:

Sample Input 0

4 0
4 4
Sample Output 0

9
Explanation 0

The queen is standing at position  on a  chessboard with no obstacles:

image

Sample Input 1

5 3
4 3
5 5
4 2
2 3
Sample Output 1

10
Explanation 1

The queen is standing at position  on a  chessboard with  obstacles:

image

The number of squares she can attack from that position is .

Sample Input 2

1 0
1 1
Sample Output 2

0
Explanation 2

Since there is only one square, and the queen is on it, the queen can move 0 squares.'''



import sys
from collections import defaultdict
from math import fabs

def check_diag(queen, obst):
    if queen[1] == obst[1]:
        return 0
    check = (queen[0] - obst[0])/(queen[1] - obst[1])
    if fabs(check) == 1.0:
        return int(check)
    else:
        return 0

def queensAttack(n, k, r_q, c_q, obstacles):
    queen = [r_q, c_q]
    res = 0
    obst_by_row = list(filter(lambda x: x[0] == r_q, obstacles))
    obst_by_col = list(filter(lambda x: x[1] == c_q, obstacles))
    obst_by_plus_diag = list(filter(lambda x: check_diag(queen, x) == 1, obstacles))
    obst_by_neg_diag = list(filter(lambda x: check_diag(queen, x) == -1, obstacles))
    
    if not obst_by_col:
        res += n-1
    else:
        obst_higher = list(filter(lambda x: x[0] > r_q, obst_by_col)) 
        if obst_higher:
            min_higher = min(obst_higher, key = lambda x: x[0])[0]
        else:
            min_higher = n+1
            
        obst_lower = list(filter(lambda x: x[0] < r_q, obst_by_col)) 
        if obst_lower:
            max_lower = max(obst_lower, key = lambda x: x[0])[0]
        else:
            max_lower = 0
            
        #print("high = {} low = {}".format(min_higher, max_lower))
        res += min_higher - max_lower - 2
            
    if not obst_by_row:
        res += n-1
    else:
        obst_higher = list(filter(lambda x: x[1] > c_q, obst_by_row)) 
        if obst_higher:
            min_higher = min(obst_higher, key = lambda x: x[1])[1]
        else:
            min_higher = n+1
            
        obst_lower = list(filter(lambda x: x[1] < c_q, obst_by_row)) 
        if obst_lower:
            max_lower = max(obst_lower, key = lambda x: x[1])[1]
        else:
            max_lower = 0
            
        #print("high = {} low = {}".format(min_higher, max_lower))
        res += min_higher - max_lower - 2
        
    # diagonals
    if not obst_by_plus_diag:
        res += n-1 - abs(r_q - c_q)
        #res += min(n - c_q, n - r_q) + min(c_q - 1, r_q - 1) # = n-1 + min(-c_q, -r_q) + min(c_q, r_q)
        #print("res = {}".format(res))
    else:
        obst_higher = list(filter(lambda x: x[0] > r_q, obst_by_plus_diag))
        if obst_higher:
            min_higher = min(obst_higher, key = lambda x: x[0])[0]
        else:
            min_higher = n+1
            
        obst_lower = list(filter(lambda x: x[0] < r_q, obst_by_plus_diag)) 
        if obst_lower:
            max_lower = max(obst_lower, key = lambda x: x[0])[0]
        else:
            max_lower = 0
            
        #print("high = {} low = {}".format(min_higher, max_lower))
        res += min_higher - max_lower - 2 - abs(r_q - c_q)
    
    if not obst_by_neg_diag:
        #print("n - c_q + r_q = {} - {} + {}".format(n, c_q, r_q))
        #res += n-1 - abs(n - c_q + r_q)
        #print("res = {}".format(res))
        #res += min(n - c_q, r_q - 1) + min(c_q - 1, n - r_q)
        # 2 variants:
        # res += n - c_q + n - r_q = 2n - c_q - r_q
        # res += r_q - 1 + c_q - 1 = r_q + c_q - 2
        res += min(n - c_q, r_q - 1)
        res += min(c_q - 1, n - r_q)
    else:
        obst_higher = list(filter(lambda x: x[0] > r_q, obst_by_neg_diag))
        if obst_higher:
            min_higher = min(obst_higher, key = lambda x: x[0])[1]
        else:
            min_higher = n+1
            
        obst_lower = list(filter(lambda x: x[0] < r_q, obst_by_neg_diag)) 
        if obst_lower:
            max_lower = max(obst_lower, key = lambda x: x[0])[1]
        else:
            max_lower = 0
            
        print("high = {} low = {}".format(min_higher, max_lower))
        print("r_q = {} c_q = {}".format(r_q, c_q))
        #res += min_higher - max_lower - 2 - abs(n - c_q + r_q)
        if max_lower != 0:
            res += max_lower - c_q - 1
        if min_higher != n+1:
            res += c_q - min_higher - 1
 
    return res
        
    
# naive        
def queensAttack_naive(n, k, r_q, c_q, obstacles):
    obst_by_row = list(filter(lambda x: x[0] == r_q, obstacles))
    obst_by_col = list(filter(lambda x: x[1] == c_q, obstacles))
    obs_dict = gen_obs_dict(obstacles)
    
    res = 0
    
    if not obst_by_col:
        res += n-1
    else:
        for row_ind in range(r_q+1, n+1):
            #if not [row_ind, c_q] in obstacles:
            key = str(row_ind) + "-" + str(c_q)
            if obs_dict[key] != -1:
                res += 1
            else:
                break
        for row_ind in range(r_q-1, 0, -1):
            #if not [row_ind, c_q] in obstacles:
            key = str(row_ind) + "-" + str(c_q)
            if obs_dict[key] != -1:
                res += 1
            else:
                break
            
    if not obst_by_row:
        res += n-1
    else:
        for col_ind in range(c_q+1, n+1):
            #if not [r_q, col_ind] in obstacles:
            key = str(r_q) + "-" + str(col_ind)
            if obs_dict[key] != -1:
                res += 1
            else:
                break
        for col_ind in range(c_q-1, 0, -1):
            #if not [r_q, col_ind] in obstacles:
            key = str(r_q) + "-" + str(col_ind)
            if obs_dict[key] != -1:
                res += 1
            else:
                break
    
    row_ind, col_ind = r_q+1, c_q+1
    while col_ind != 0 and row_ind != 0 and col_ind != n+1 and row_ind != n+1:
        #if not [row_ind, col_ind] in obstacles:
        key = str(row_ind) + "-" + str(col_ind)
        if obs_dict[key] != -1:
            res += 1
            row_ind += 1
            col_ind += 1
        else:
            break
            
    row_ind, col_ind = r_q-1, c_q+1
    while col_ind != 0 and row_ind != 0 and col_ind != n+1 and row_ind != n+1:
        #if not [row_ind, col_ind] in obstacles:
        key = str(row_ind) + "-" + str(col_ind)
        if obs_dict[key] != -1:
            res += 1
            row_ind -= 1
            col_ind += 1
        else:
            break
            
    row_ind, col_ind = r_q+1, c_q-1
    while col_ind != 0 and row_ind != 0 and col_ind != n+1 and row_ind != n+1:
        #if not [row_ind, col_ind] in obstacles:
        key = str(row_ind) + "-" + str(col_ind)
        if obs_dict[key] != -1:
            res += 1
            row_ind += 1
            col_ind -= 1
        else:
            break        
            
    row_ind, col_ind = r_q-1, c_q-1
    while col_ind != 0 and row_ind != 0 and col_ind != n+1 and row_ind != n+1:
        #if not [row_ind, col_ind] in obstacles:
        key = str(row_ind) + "-" + str(col_ind)
        if obs_dict[key] != -1:
            res += 1
            row_ind -= 1
            col_ind -= 1
        else:
            break        
 
    return res
            
def gen_obs_dict(obstacles):
    dict_out = defaultdict(int)    
    for obs in obstacles:
        row, col = obs[0], obs[1]
        key = str(row) + "-" + str(col)
        dict_out[key] = -1
        
    return dict_out

if __name__ == "__main__":
    n, k = [int(x) for x in input().strip().split(' ')]
    r_q, c_q = [int(x) for x in input().strip().split(' ')]
    obstacles = []
    for obstacles_i in range(k):
        obstacles_t = [int(obstacles_temp) for obstacles_temp in input().strip().split(' ')]
        obstacles.append(obstacles_t)
    result = queensAttack_naive(n, k, r_q, c_q, obstacles)
    print(result)


