// For problem details, go to: https://www.hackerrank.com/challenges/camelcase/problem

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main() {
	string s;
	cin >> s;

	int i = 1;

	int length = s.length();

	for (int j = 0; j <= length; j++) {
		char c = s[j];
		if (isupper(c)) {
			i++;
		}
	}

	cout << i;


	return 0;

}