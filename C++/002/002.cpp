#include <iostream>
#include <vector>

/*
* Problem #: 002
* Date Attempted: 05/28/20
* Date Solved: 05/28/20
*
* By considering the terms in the Fibonacci sequence whose values do not exceed four million,
* find the sum of the even-valued terms.
*
*	Answer: 4613732
*/

 std::vector<long> genFib() {
    long next = 1;
    std::vector<long> fibs{1};
    while (next < 4000000) {
        fibs.push_back(next);
        next = fibs[fibs.size() - 1] + fibs[fibs.size() - 2];
    }
    return fibs;
}


int main()
{
    std::vector<long> fibs = genFib();
    long long sum = 0;
    for (auto l : fibs) {
        if (l % 2 == 0) {
            sum += l;
        }
    }
    std::cout << sum << std::endl;
}