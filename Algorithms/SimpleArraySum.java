/**
 * Input Format
 * The first line contains an integer, N, denoting the size of the array. The second line contains
 * N space-separated integers representing the array's elements.
 *
 * Output Format
 * Print the sum of the array's elements as a single integer.
 *
 * Sample Input
 * 6
 * 1 2 3 4 10 11
 *
 * Sample Output
 * 31
 *
 * Explanation
 * We print the sum of the array's elements, which is: 1 + 2 + 3 + 4 + 10 + 11.
 */

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  static int simpleArraySum(int n, int[] ar) {
    // Complete this function
    int sum = 0;
    for (int i : ar) {
      sum = sum + i;
    }

    return sum;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int[] ar = new int[n];
    for(int ar_i = 0; ar_i < n; ar_i++){
      ar[ar_i] = in.nextInt();
    }
    int result = simpleArraySum(n, ar);
    System.out.println(result);
  }
}
