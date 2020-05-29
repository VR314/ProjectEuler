import java.util.ArrayList;

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

public class _002 {
    public static ArrayList<Long> fibs;

    public static void main(String[] args) {
        fibs = new ArrayList<Long>();
        fibs.add(1L);
        fibs.add(1L);
        while (true) {
            long x = nextFib();
            if (x < 4000000) {
                fibs.add(x);
            } else {
                break;
            }
        }

        long sum = 0;
        for (long l : fibs) {
            if (l % 2 == 0) {
                sum += l;
            }
        }
        System.out.println(sum);
    }

    static long nextFib() {
        return (long) fibs.get(fibs.size() - 1) + (long) fibs.get(fibs.size() - 1);
    }
}