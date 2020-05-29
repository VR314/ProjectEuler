using System;
using System.Collections.Generic;

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

namespace _002
{
    class Program
    {
        static List<long> fibs;
        static void Main(string[] args)
        {
            fibs = new List<long>();
            fibs.Add(1);
            fibs.Add(1);
            while(true){
                long x = nextFib();
                if(x < 4000000){
                    fibs.Add(x);
                } else {
                    break;    
                }
            }

            long sum = 0;
            foreach(long l in fibs){
                if(l % 2 == 0){
                    sum += l;
                }
            }
            Console.WriteLine(sum);

        }

        static long nextFib(){
            return fibs[fibs.Count - 1] + fibs[fibs.Count - 2];
        }
    }
}
