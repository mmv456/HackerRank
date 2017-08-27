// Problem details found at: https://www.hackerrank.com/challenges/migratory-birds/problem

#include <bits/stdc++.h>

using namespace std;


int main() {

	int size = 0;
	cin >> size;

	int birds[size];

	for (int i = 0; i < size; i++) {
		cin >> birds[i];
	}

	int type[5] = { 0, 0, 0, 0, 0 };


	for (int j = 0; j < size; j++) {
		type[birds[j] - 1]++;
	}

	int max = 0;

	for (int k = 0; k < 5; k++) {
		if (type[k] > type[max]) { max = k; }
	}

	cout << max + 1 << endl;

	return 0;
}
