# -*- coding: utf-8 -*-
"""
The provided code stub will read in a dictionary containing key/value 
pairs of name:[marks] for a list of students. Print the average of the 
marks array for the student name provided, showing 2 places after the 
decimal.

Example

marks key:value pairs are
'alpha': [20,30,40]
'beta': [30,50,70]
query_name = 'beta'

The query_name is 'beta'. 
beta's average score is (30 + 50 + 70)/3 = 50.0.

Input Format

The first line contains the integer n, the number of students' records. 
The next n lines contain the names and marks obtained by a student, 
each value separated by a space. The final line contains query_name, 
the name of a student to query.

Constraints
- 2 <= n <= 10
- 0 <= marks[i] <= 100
- length of marks arrays = 3

Output Format

Print one line: The average of the marks obtained by the particular 
student correct to 2 decimal places.

Sample Input 0
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0
56.00

Explanation 0
Marks for Malika are {52,56,60} whose average is (52+56+60)/3 = 56

Sample Input 1
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample Output 1
26.50
"""

# Dictionary String -> List-of-Numbers
# return the list of scores in the dictionary for the given name
def get_scores(dict, name):
    return dict[name]

# List_of_Numbers -> Number
# get the average of the list of scores
def get_average(lon):
    total = 0
    for x in lon:
        total += x
    return total/3

# Dict String -> Number
# given a dictionary of names-scores and a name, get the average score
def get_average_score(dict, name):
    scores = get_scores(dict, name)
    average_score = get_average(scores)
    return average_score

# Test cases
def test_problem():
    d1 = {'Harsh': [25.0, 26.5, 28.0], 'Anurag': [26.0, 28.0, 30.0]}
    
    l1 = [25.0, 26.5, 28.0]
    l2 = [26.0, 28.0, 30.0]
    
    assert get_scores(d1, "Harsh") == l1, "Should be [25.0, 26.5, 28.0]"
    assert get_scores(d1, "Anurag") == l2, "Should be [26.0, 28.0, 30.0]"
    
    assert get_average(l1) == 26.5, "Should be 26.5"
    assert get_average(l2) == 28.0, "Should be 28.0"
    
    assert get_average_score(d1, "Harsh") == 26.5, "Should be 26.5"
    assert get_average_score(d1, "Anurag") == 28.0, "Should be 28.0"

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #test_problem()
    print(round(get_average_score(student_marks, query_name), 2))