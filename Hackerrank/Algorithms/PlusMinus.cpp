/**
Plus Minus

Given an array of integers, calculate which fraction of its elements are positive, which fraction of its 
elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value 
of each fraction on a new line.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
though answers with absolute error of up to 10^-4 are acceptable.


Input Format
The first line contains an integer, N, denoting the size of the array.
The second line contains N space-separated integers describing an array of numbers (a0, a1, a2, ..., an-1).


Output Format
You must print the following 3 lines:
1. A decimal representing of the fraction of positive numbers in the array compared to its size.
2. A decimal representing of the fraction of negative numbers in the array compared to its size.
3. A decimal representing of the fraction of zeroes in the array compared to its size.


Sample Input
6
-4 3 -9 0 4 1


Sample Output
0.500000
0.333333
0.166667


Explanation
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The respective fractions of positive numbers, negative numbers and zeroes are
3/6 = 0.500000, 2/6 = 0.333333 and 1/6 = 0.166667, respectively.

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int n;
	cin >> n;


	float pos = 0;
	float neg = 0;
	float zero = 0;

	// get the values
	for (int i = 0; i < n; i++) {
		int number;
		cin >> number;

		pos += (number > 0);
		neg += (number < 0);
		zero += (number == 0);
	}


	cout << pos / n << endl;
	cout << neg / n << endl;
	cout << zero / n << endl;


	return 0;
}