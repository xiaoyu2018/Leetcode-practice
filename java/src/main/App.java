package main;
import java.util.Arrays;
import java.util.Scanner;

import main.algorithm.*;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        String[] nums = sc.nextLine().strip().split(" ");
        int target = sc.nextInt();
        
        int[] revokes = new int[nums.length];
        int i=0;
        for (String n : nums) {
            revokes[i++] = Integer.parseInt(n);
        }
        
        System.out.println(new HW412_1().solve(revokes, target));
    }
}
