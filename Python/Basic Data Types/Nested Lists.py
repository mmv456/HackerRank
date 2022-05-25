# -*- coding: utf-8 -*-
"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

Example
records = [["chi",20.0], ["beta",50.0], ["alpha",50.0]]
The ordered list of scores is [20.0,50.0], so the second lowest 
score is 50.0. 
There are two students with that score: ["beta","alpha"]. 
Ordered alphabetically, the names are printed as:
    alpha
    beta
    
Input Format
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints
- 2 <= N <= 5
- There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and 
print each one on a new line.

Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0
Berry
Harry

Explanation 0
There are 5 students in this class whose names and grades are assembled 
to build the following list:
python students = [['Harry', 37.21], 
                   ['Berry', 37.21], 
                   \['Tina', 37.2], 
                   ['Akriti', 41], 
                   ['Harsh', 39]]
The lowest grade of 37.2 belongs to Tina. 
The second lowest grade of 37.21 belongs to both Harry and Berry, 
so we order their names alphabetically and print each name on a new line.
"""

# Dict -> List
# given a dictionary of score-name pairs, return a list of scores
def get_score_list(dict):
    return list(dict.keys())

# List-of-Numbers -> Number
# return the lowest number in the list
def get_lowest_score(lon):
    lowest_score = lon[0]
    for x in lon:
        if x <= lowest_score:
            lowest_score = x
    return lowest_score

# List-of-Numbers Number -> List-of-Numbers
# remove the given number from the list
def remove_lowest(lon, lowest):
    new_list = []
    for x in lon:
        if x != lowest:
            new_list.append(x)
    return new_list

# Dict Number -> List
# return the values in the dict corresponging to the given scor
def get_values(dict, num):
    return dict[num]

# list-of-Strings -> List-of-Strings
# alpabetically order the list of strings
def order_list(l):
    return sorted(l)

# Dict -> List
# returns the list of names for people who have the second lowest score
def get_names(dict):
    l = []
    all_scores_list = get_score_list(dict)
    lowest_score = get_lowest_score(all_scores_list)
    cleaned_list = remove_lowest(all_scores_list, lowest_score)
    second_lowest_score = get_lowest_score(cleaned_list)
    l = get_values(dict, second_lowest_score)
    l = order_list(l)
    return l

# Tests
def test_problem():
    d1 = {10.0: ['A', 'B']}
    d2 = {5.0: ['C'], 6.0: ['D'], 3.0: ['E']}
    d3 = {15.0: ['F'], 6.0: ['G', 'H'], 3.0: ['E']}
    
    l1 = [10.0]
    l2 = [5.0, 6.0, 3.0]
    l3 = [15.0, 6.0, 3.0]
    
    assert get_score_list(d1) == l1, "Should be [10.0]"
    assert get_score_list(d2) == l2, "Should be [5.0, 6.0, 3.0]"
    assert get_score_list(d3) == l3, "Should be [15.0, 6.0, 3.0]"
    
    assert get_lowest_score(l1) == 10.0, "Should be 10.0"
    assert get_lowest_score(l2) == 3.0, "Should be 3.0"
    assert get_lowest_score(l3) == 3.0, "Should be 3.0"
    
    assert remove_lowest(l1, get_lowest_score(l1)) == [], "Should be []"
    assert remove_lowest(l2, get_lowest_score(l2)) == [5.0, 6.0], "Should be [5.0, 6.0]"
    assert remove_lowest(l3, get_lowest_score(l3)) == [15.0, 6.0], "Should be [15.0, 6.0]"
    
    assert order_list(['A', 'B']) == ['A', 'B'], "Should be ['A', 'B']"
    assert order_list(['B', 'A']) == ['A', 'B'], "Should be ['A', 'B']"
    
    assert get_values(d1, 10.0) == ['A', 'B'], "Should be ['A', 'B']"
    
    

if __name__ == '__main__':
    dict = {}
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict.setdefault(score, [])
        dict[score].append(name)
    #test_problem()
    for x in get_names(dict):
        print(x)