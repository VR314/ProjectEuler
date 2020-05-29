
let half input = int32(input) / 2

let findLargestPrimeFactor l:int64 =
    let mutable input:int64 = l
    let mutable again = true
    while again do
        again <- false
        for i = 2 to (half input) do
            if input % int64(i) = 0L then
                input <- input / int64(i)
                again <- true
    input

printfn "%i" (findLargestPrimeFactor 600851475143L)