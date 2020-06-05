let sumDivisors n = 
    let mutable divisors = [1]
    for i in 2.. int(sqrt (float n)) + 1 do
        if n % i = 0 then 
            if n/i = i then divisors <- List.append divisors [i]
            else divisors <- List.append divisors [n/i; i]
    List.sum divisors


let abundants = seq {
    for i in 12..28123 do
        if sumDivisors i > i then yield i
}

(*
let written = seq {
  let len = Seq.length abundants
  for i in 0..len do
    for j in i..len do 
        yield i + j
}
*)

let mutable writtenSum:bigint = 0I
let len = Seq.length abundants
for a in abundants do
    writtenSum <- writtenSum + bigint(a) * bigint(Seq.length abundants - 1)
    printfn "%i" (len - (Seq.findIndex (fun x -> x = a) abundants))

let all = seq {
  for i in 1..28132 do yield i
}

(*
let canBeWritten x =
    let mutable result = false 
    let possibles = Seq.filter (fun y -> y < x/2) abundants
    let second = Seq.filter (fun y -> y > x/2 && y < x) abundants
    for poss in possibles do
        if Seq.contains (x - poss) second then result <- true
    result
*)

let bigint (x:int) = bigint(x)

let sum:bigint = bigint(Seq.sum all) - writtenSum
printfn "%A" (sum)