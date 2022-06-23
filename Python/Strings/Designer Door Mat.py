# -*- coding: utf-8 -*-
"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a 
new door mat with the following specifications:

- Mat size must be N * M. (N is an odd natural number, and M is 3 times N.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use |, . and - characters.


Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
    
    
Input Format
A single line containing the space separated values of N and M.

Constraints
- 5 < N < 101
- 15 < M < 303

Output Format
Output the design pattern.

Sample Input
9 27

Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

if __name__ == '__main__':
    n, m = int(input()), int(input())
    # n is the # of rows
    # m is the number of columns
    
    sys.stdout.write('Hello\n')
    sys.stdout.write(str(n))
    sys.stdout.write('\n')
    sys.stdout.write(str(m))
    sys.stdout.write('\n')
    
    middle_row = (n // 2)
    middle_col = (m // 2)
    
    for row in range(n):
        
        for column in range(m):
            if ((row == middle_row) & (column == middle_col)):
                sys.stdout.write('X')
            else:
                sys.stdout.write('-')
            
        sys.stdout.write('\n')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    