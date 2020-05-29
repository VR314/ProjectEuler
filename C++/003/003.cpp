#include <iostream>

/*
*	Problem #: 003
*	Date Attempted: 05/28/20
*	Date Solved: 05/28/20
*
*	What is the largest prime factor of the number 600851475143 ?
*
*	Answer: 6857
*/

int main()
{
    bool again = true;
    long long input = 600851475143L;
    while (again) {
        again = false;
        for (int i = 2; i < sqrt(input); i++) {
            if (input % i == 0) {
                input /= i;
                again = true;
            }
        }
    }
    std::cout << input << std::endl;
}