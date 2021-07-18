(*
*	Problem #: 025
*	Date Attempted: 03/24/21
*	Date Solved: 
*
*	What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
*
*	Answer: 
*)



let run = 
    let digits num:int = String.length ((num.ToString())) + 1
    let mutable uno, dos, tres = 1,1,2
    let mutable index = 3
    while digits(tres) <> 3 do
        uno <- dos
        dos <- tres
        tres <- uno + dos
        index <- index+1
    index

printfn "ans: %i" run
