#include <iostream>
#include <vector>

/*
*	Problem #: 010
*	Date Attempted: 05/30/20
*	Date Solved: 05/30/20
*
*	Find the sum of all the primes below two million.
*
*	Answer: 142913828922
*/

long long primeSum(long long limit) {
    std::vector<long long> primes{ 2 };
    long p{};
    for (p = 3; primes.back() < limit; p++) {
        bool divis = false;
        for (long prime : primes) {
            if (p % prime == 0) {
                divis = true;
            }
        }
        if (!divis) {
            primes.push_back(p);
        }
    }
    
    long long sum{ 0 };
    for (long long l : primes) {
        sum += l;
    }
    sum -= primes.back();
    return sum;
}

int main()
{
    std::cout << primeSum(2000000L) << std::endl;
}
