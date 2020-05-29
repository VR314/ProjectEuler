(*
*	Problem #: 002
*	Date Attempted: 05/28/20
*	Date Solved: 05/28/20
*
*	By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
*   find the sum of the even-valued terms.
*
*	Answer: 4613732
*)

let rec fib n = if n < 2 then 1 else fib (n-2) + fib(n-1)
let values = seq {
    let mutable n = 0
    while fib n < 4000000 do 
        n <- n + 1 
        yield fib n
}

let isEven x = x % 2 = 0

printfn "%i" (Seq.filter isEven values |> Seq.sum)
