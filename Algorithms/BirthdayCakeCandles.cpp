/**
Birthday Cake Candles

Colleen is turning n years old! Therefore, she has n candles of various heights on 
her cake, and candle i has height heighti. Because the taller candles tower over the 
shorter ones, Colleen can only blow out the tallest candles.

Given the heighti, for each individual candle, find and print the number of candles 
she can successfully blow out.


Input Format
The first line contains a single integer, n, denoting the number of candles on the cake.
The second line contains n space-separated integers, where each integer i describes the 
height of candle i.


Constraints
1 <= n <= 10^5
1 <= heighti <= 10^7


Output Format
Print the number of candles Colleen blows out on a new line.


Sample Input 0
4
3 2 1 3

Sample Output 0
2

Explanation 0
We have one candle of height 1, one candle of height 2, and two candles of height 3.
Colleen only blows out the tallest candles, meaning the candles where height = 3. Because
there are 2 such candles, we print 2 on a new line.

*/

#include <bits/stdc++.h>

using namespace std;

int birthdayCakeCandles(int n, vector <int> ar) {
	// Complete this function
	int highest = 0;
	// go through the function, find the biggest value
	for (int i : ar) {
		if (i > highest) {
			highest = i;
		}
	}

	// go through the array, find the number of times the
	// biggest value appears in the array
	int number = 0;
	for (int i : ar) {
		if (i == highest) {
			number += 1;
		}
	}

	return number;


}

int main() {
	int n;
	cin >> n;
	vector<int> ar(n);
	for (int ar_i = 0; ar_i < n; ar_i++) {
		cin >> ar[ar_i];
	}
	int result = birthdayCakeCandles(n, ar);
	cout << result << endl;
	return 0;
}
