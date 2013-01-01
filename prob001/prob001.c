/*
===========================
Project Euler - Problem 001
---------------------------
Description: Find the sum of all the multiples of 3 or 5 below 1000.
===========================
*/

#include<stdio.h>

int main() {
    int i, total = 0;
    for (i = 1; i < 1000; ++i) {
        if (i % 3 == 0 || i % 5 == 0) {
            total += i;
        }
    }
    printf("%d\n", total);
}

