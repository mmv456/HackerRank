// Problem details found at https://www.hackerrank.com/challenges/time-conversion/problem


#include <bits/stdc++.h>
#include <string>

using namespace std;



void changeAM(int *h) {
	*h = 00;
}

void changePM(int *h) {
	*h += 12;
}


int main() {
	string s;
	cin >> s;

	int stringLength = s.length();
	int hour = stoi(s.substr(0, 2));

	string time = s.substr(stringLength - 2);


	if (time == "AM" && hour == 12) {
		changeAM(&hour);
	}

	if (time == "PM" && hour != 12) {
		changePM(&hour);
	}

	if (hour <= 9) {
		cout << 0;
	}


	cout << hour;
	cout << s.substr(2, 6);
	return 0;
}
