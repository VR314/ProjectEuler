using System;
using System.Collections.Generic;
using System.Linq;


/*
*	Problem #: 003
*	Date Attempted: 05/28/20
*	Date Solved: 05/28/20
*
*	What is the largest prime factor of the number 600851475143 ?
*
*	Answer: 6857
*/

namespace _003
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(FindLargestPrimeFactor(600851475143));
        }

        static bool isPrime(long d)
        {
            for (int i = 2; i < Math.Sqrt(d); i++)
            {
                if (d % i == 0)
                {
                    return false;
                }
            }
            return true;
        }

        static long FindLargestPrimeFactor(long l)
        {
            while (true)
            {
                int i;
                for(i = 2; i <= Math.Sqrt(l); i++)
                {
                    if(l % i == 0)
                    {
                        l = l / i;
                    }
                }
                if(i >= Math.Sqrt(l)) //if l is prime
                {
                    break;
                }
            }

            return l;
        }
    }
}
