#include <iostream>
#include <vector>

/*
*	Problem #: 007
*	Date Attempted: 05/29/20
*	Date Solved: 05/29/20
*
*	What is the 10 001st prime number?
*
*	Answer: 104743
*/

long nthPrime(int n) {
    int count = 1;
    std::vector<long> primes{2};
    long p;
    for (p = 3; count < n; p++) {
        bool divis = false;
        for (long prime : primes) {
            if (p % prime == 0) {
                divis = true;
            }
        }
        if (!divis) {
            primes.push_back(p);
            count++;
            std::cout << count << std::endl;
        }
    }
    return primes.back();
}


int main()
{
    std::cout << "ans: " << nthPrime(10001) << std::endl; //should be 13
}