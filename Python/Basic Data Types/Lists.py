# -*- coding: utf-8 -*-
"""
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands 
where each command will be of the  types listed above. Iterate through each 
command in order and perform the corresponding operation on your list.

Example
N = 4
append 1
append 2
insert 3 1
print

- append 1: Append 1 to the list, arr = [1].
- append 2: Append 2 to the list, arr = [1,2].
- insert 3 1: Insert 3 at index 1, arr = [1,3,2].
- print: Print the array.

Output:
[1, 3, 2]

Input Format
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described 
above.

Constraints
- The elements added to the list must be integers.

Output Format
For each command of type print, print the list on a new line.

Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

# List -> List
# takes the list of commands and gets the list of results
def apply(commands):
    output = []
    return output



# List Number Number -> List
# inserts the integer into the given position in the list
def insert(input_list, integer, position):
    new_list = []
    for x in range(len(input_list)):
        if x == position:
            new_list.append(integer)
            new_list.append(input_list[x])
        else:
            new_list.append(input_list[x])
    return new_list

# List Number -> List
# removes the first occurrence of the given number
def remove(input_list, number):
    for x in range(len(input_list)):
        if input_list[x] == number:
            return input_list
            
    return input_list

# List Number -> List
# inserts the given integer at the end of the list.
def append(output, number):
    return output

# List -> List
# sorts the list form low to high
def sort(output):
    return output

# List -> List
# pops the last element from the list
def pop(output):
    return output

# List -> List
# reverses the list
def reverse(output):
    return output

# Test cases
def test_problem():
    
    l1 = [1,2,4]
    l2 = [1,2,1,3]
    
    assert insert(l1, 3, 2) == [1,2,3,4], "Insert function in middle not right"
    assert insert(l1, 0, 0) == [0,1,2,4], "Insert function in beginning not right"
    
    assert remove(l1, 1) == [2,4], "Remove function in beginning not working"
    assert remove(l1, 2) == [1,4], "Remove function in middle not working"
    assert remove(l1, 4) == [1,2], "Remove function in end not working"
    assert remove(l1, 3) == [1,2,4], "Remove function for missing input not working"
    assert remove(l2, 1) == [2,1,3], "Remove function for duplicates not working"
    
    
    
if __name__ == '__main__':
    # take in the inputs
    #n = int(input())
    #list_of_commands = []
    #for _ in range(n):
    #    list_of_commands.append(input())
    # send the inputs somewhere
    # get the result back
    #print(list_of_commands)
    test_problem()