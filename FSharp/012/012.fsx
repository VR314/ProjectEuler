
(*
*	Problem #: 012
*	Date Attempted: 05/30/20
*	Date Solved: 05/30/20
*
*	What is the value of the first triangle number to have over 500 divisors?
*
*	Answer: 76576500
*)

let isValid value = 
    let mutable numFactors = 1
    for i in 1..int(sqrt(float(value))) + 1 do
        if value % i = 0 then numFactors <- numFactors + 1
    numFactors > 250

let mutable triangulars = [1]
for i in 2..100000 do
    triangulars <- List.append triangulars [(triangulars.Item(i-2) + i)]
    if isValid (triangulars.Item (triangulars.Length - 1)) then printfn "%i" (triangulars.Item (triangulars.Length - 1))