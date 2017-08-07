/**
 * Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges,
 * awarding points on a scale from 1 to 100 for three categories: problem clarity, originality,
 * and difficulty.
 *
 * We define the rating for Alice's challenge to be the triplet A = (a0, a1, a2), and the
 * rating for Bob's challenge to be the triplet B = (b0, b1, b2).
 *
 * Your task is to find their comparison points by comparing a0 with b0, a1 with b1, and a2 with
 * b2.
 *  - If ai > bi, then Alice is awarded 1 point
 *  - If ai < bi, then Bob is awarded 1 point
 *  - If ai = bi, then neither person receives a point
 *
 * Comparison points is the total points a person earned.
 *
 * Given A and B, can you compare the two challenges and print their respective comparison points?
 *
 * Input format
 * The first line contains 3 space-separated integers, a0, a1, and a2, describing the respective
 * values in triplet A.
 * The second line contains 3 space-separated integers, b0, b1, and b2, describign the respective
 * values in triplet B.
 *
 * Constraints
 * 1 <= ai <= 100
 * 1 <= bi <= 100
 *
 * Output format
 * Print two space-separated integers denoting the respective comparison points earned by Alice and
 * Bob.
 *
 * Sample Input
 * 5 6 7
 * 3 6 10
 *
 * Sample Output
 * 1 1
 */


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {


  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int[] alice = new int[3];
    int[] bob = new int[3];

    for(int i = 0; i < 3; i++) {
      alice[i] = in.nextInt();
    }
    for(int i = 0; i < 3; i++) {
      bob[i] = in.nextInt();
    }

    int aliceScore = 0;
    int bobScore = 0;

    for(int i = 0; i < 3; i++) {
      if(alice[i] > bob[i]) {
        aliceScore += 1;
      }
      else if(alice[i] < bob[i]) {
        bobScore += 1;
      }
    }

    System.out.printf("%d %d", aliceScore, bobScore);



  }
}
