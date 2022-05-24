# -*- coding: utf-8 -*-
"""
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] 
of n integers each separated by a space.

Constraints
- 2 <= n <= 10
- -100 <= A[i] <= 100

Output Format
Print the runner-up score.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5

Explanation 0
Given list is [2,3,6,6,5]. 
The maximum score is 6, second maximum is 5. 
Hence, we print 5 as the runner-up score.
"""

# Array -> Number
# find the largest number
def find_largest_number(array):
    largest = array[0]
    for x in array:
        if x >= largest:
            largest = x
    return largest

# Array Number -> List
# remove the largest number from the array
def remove_largest_number(array, number):
    running_list = []
    for x in array:
        if x != number:
            running_list.append(x)
    return running_list

# Array -> Number
# return the second highest number in the array
def get_second_highest_number(array):
    largest_number = find_largest_number(array)
    leftover_list = remove_largest_number(array, largest_number)
    return find_largest_number(leftover_list)

def test_array():
    assert find_largest_number([1,2,3,4]) == 4, "Should be 4"
    assert remove_largest_number([1,2,3,4], 4) == [1,2,3], "Should be [1,2,3]"
    test_list1 = [2,3,6,6,5]
    assert find_largest_number(test_list1) == 6, "Should be 6"
    assert remove_largest_number(test_list1, 6) == [2,3,5], "Should be [2,3,5"
    assert get_second_highest_number(test_list1) == 5, "Should be 5"
    assert get_second_highest_number([-2, -5]) == -5, "Should be -5"
    

if __name__ == "__main__":
    #test_array()
    #print(get_second_highest_number([-2, -5]))
    #print("Everything passed")
    n = int(input())
    arr = map(int, input().split())
    l = []
    for x in arr:
        l.append(x)
    print(get_second_highest_number(l))