
/*
*	Problem #: 003
*	Date Attempted: 05/28/20
*	Date Solved: 05/29/20
*
*	What is the largest prime factor of the number 600851475143 ?
*
*	Answer: 6857
*/

public class _003 {
    public static void main(String[] args) {
        boolean again = true;
        long input = 600851475143L;
        while (again) {
            again = false;
            for (int i = 2; i < Math.sqrt(input); i++) {
                if (input % i == 0) {
                    again = true;
                    input /= i;
                }
            }
        }

        System.out.println(input);
    }
}