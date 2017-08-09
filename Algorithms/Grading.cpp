// Go here for explanation: https://www.hackerrank.com/challenges/grading/problem

#include <bits/stdc++.h>

using namespace std;

int nextMultiple(int grade) {
	if (grade % 5 == 0) {
		return grade;
	}

	else if ((grade + 1) % 5 == 0) {
		return grade + 1;
	}

	else if ((grade + 2) % 5 == 0) {
		return grade + 2;
	}

	else {
		return grade;
	}

}

int main() {
	int n; // # of grades
	cin >> n;
	vector<int> grades(n); // grades
	for (int i = 0; i < n; i++) {
		cin >> grades[i];
	}


	for (int i : grades) {
		if (i >= 38) {
			cout << nextMultiple(i) << endl;
		}
		else {
			cout << i << endl;
		}
	}



	return 0;
}
