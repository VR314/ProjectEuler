open System

(*
*	Problem #: 003
*	Date Attempted: 05/28/20
*	Date Solved: 05/29/20
*
*	What is the largest prime factor of the number 600851475143 ?
*
*	Answer: 6857
*)

let sqrt input = Math.Sqrt(float(input))

let find input:int64 = 
    let mutable temp = (input) 
    let mutable again = true
    while again do 
        again <- false
        for i = 2 to int(sqrt temp) do 
            if temp % int64(i) = 0L && int64(i) < temp then
                again <- true
                //printfn "%i / %i" temp i
                temp <- temp / int64(i)
            else do ()
    temp


let value = find 600851475143L
printfn "%i" value