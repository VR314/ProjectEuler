(*
*	Problem #: 009
*	Date Attempted: 05/29/20
*	Date Solved: 05/29/20
*
*	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
*   Find the product abc.
*
*	Answer: 31875000
*)

let pythTriple a b =
    let c = pown a 2 + pown b 2
    if (float32(c) |> sqrt |> floor) = (float32(c) |> sqrt) then float32(c) |> sqrt
    else float32(0.0)

let triples = seq {
    for a in 2..998 do
        for b in a..998 do
            let c = pythTriple a b
            if c <> float32(0.0) then 
                yield (a, b, int(c))
}

let mutable winningTuple = (0,0,0)
for tuple in triples do
    let a, b, c = tuple
    if a + b + c = 1000 && pown a 2 + pown b 2 = pown c 2 then winningTuple <- tuple

let a, b, c = winningTuple
printfn "a = %i b = %i c = %i" a b c

a*b*c