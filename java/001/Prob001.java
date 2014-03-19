/*
===========================
Project Euler - Problem 001
---------------------------
Description: Find the sum of all the multiples of 3 or 5 below 1000.
===========================
*/

public class Prob001 {
    public static void main(String[] args) {
        int total = 0;
        for (int i = 0; i < 1000; ++i) {
            if (i % 3 == 0 || i % 5 == 0) {
                total += i;
            }
        }
        System.out.println(total);
    }
}
