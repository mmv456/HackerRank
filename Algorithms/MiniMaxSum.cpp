// Problem details can be found at https://www.hackerrank.com/challenges/mini-max-sum/problem

#include <bits/stdc++.h>

using namespace std;

int main() {
	vector<int> arr(5);
	for (int arr_i = 0; arr_i < 5; arr_i++) {
		cin >> arr[arr_i];
	}

	long max = 0;
	long min = 1000000000;
	long sum = 0;

	for (int i : arr) {
		sum += i;
		if (min > i) { min = i; }
		if (max < i) { max = i; }
	}

	cout << (sum - max);
	cout << " ";
	cout << (sum - min) << endl;

	return 0;
}
