// Problem found at: https://www.hackerrank.com/challenges/cpp-input-and-output/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	int numbers[3];

	for (int i = 0; i < 3; i++) {
		cin >> numbers[i];
	}

	int sum = 0;

	for (int j : numbers) {
		sum += j;
	}

	cout << sum;

	return 0;
}
