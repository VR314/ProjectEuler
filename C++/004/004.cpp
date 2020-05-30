#include <iostream>
#include <sstream>

/*
*	Problem #: 004
*	Date Attempted: 05/28/20
*	Date Solved: 05/29/20
*
*	Find the largest palindrome made from the product of two 3-digit numbers.
*
*	Answer: 906609
*/

bool isValid(long l) {
	std::string s = std::to_string(l);
	if (s.length() != 6) {
		return false;
	}
	for (int i = 0; i < s.length() / 2; i++) {
		if (s[i] != s[s.length() - i - 1]) {
			return false;
		}
	}
	return true;
}

int main() {
	long largest = 0;
	for (int x = 999; x >= 100; x--) { //kinda slow... (made it 900 for the test)
		for (int y = 999; y >= 100; y--) {
			if (isValid(x * y) && x * y > largest) {
				largest = x * y;
			}
			std::cout << x << " * " << y << " = " << x*y << std::endl;
		}
	}
	std::cout << largest << std::endl;
}