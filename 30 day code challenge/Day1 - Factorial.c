#include <stdio.h>

int main() {
    int Num;
    int i;
    int total = 1;

// Ask the user to type a number
    printf("Type a number: \n");

// Get and save the number the user types
    scanf("%d", &Num);
    for (i = 1; i <= Num; ++i)
    {
        total = total * i;
    }
    printf("Factorial = %d",total);
    return 0;
}