
(*
*	Problem #: 021
*	Date Attempted: 06/04/20
*	Date Solved: 06/04/20
*
*	Evaluate the sum of all the amicable numbers under 10000.
*
*	Answer: 31626
*)

let sumDivisors n = 
    let mutable divisors = [1]
    for i in 2.. int(sqrt (float n)) + 1 do
        if n % i = 0 then divisors <- List.append divisors [n/i; i]
    List.sum divisors

let amicableNumber (x) = 
    let y = sumDivisors x 
    if sumDivisors y = x  && y <> x && y <> 1 then x
    else 0

let solutionSet = seq {
    for i in 1..10000 do
        yield amicableNumber i
}

printfn "%i" (Seq.sum solutionSet)