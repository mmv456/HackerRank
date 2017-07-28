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
