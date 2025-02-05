open System
open System.Collections.Generic

type LinkedList<'T>=
    | Empty
    | Node of 'T * LinkedList<'T>

let Head =
    function
    | Empty -> failwith "Lista pusta - nie można pobrać głowy"
    | Node(Head, _) -> Head

let Tail =
    function
    | Empty -> failwith "Lista pusta - nie można pobrać ogona"
    | Node(Tail, _) -> Tail

let addHead value list = 
    Node(value, list)

let rec printList list =
    match list with
    | Empty -> ()
    | Node (value, next) -> 
        printf "%A" value
        printList next // rekurencja


    // Napisz funkcję, która tworzy listę łączoną na podstawie zwykłej listy (List<'T>)
let rec fromList = 
    function
        | [] -> Empty
        | x :: xs -> Node(x, fromList xs)

    //Napisz funkcję, która sumuje elementy listy zawierającej liczby całkowite.

let rec sumList =
    function
        | Empty -> 0
        | Node(H,T) -> H + sumList T

    //funkcja do wczytywania listy od user\
let rec userInputList () =
    printf "Podaj elementy listy oddzielone spacją: "
    let input = Console.ReadLine()
    let items = 
        input.Split(' ')
        |> Array.choose(fun x -> 
            match Int32.TryParse(x) with
            | (true, v) -> Some v
            | _ -> None)

        |> Array.toList
    fromList items


    //Napisz funkcję, która znajduje maksymalny i minimalny element w liście liczbowej.
let rec findMinMaxRec list minSoFar maxSoFar =
    match list with
    | Empty -> (minSoFar, maxSoFar)
    | Node(head, tail) -> findMinMaxRec tail (min head minSoFar) (max head maxSoFar)

let findMinMax list =
    match list with
    | Empty -> None
    | Node(head, tail) -> Some (findMinMaxRec tail head head)



//wywołanie
[<EntryPoint>]
let main argv = 
    let mutable userList = Empty

    userList <- userInputList()

    printf"n\Lista podana przez uzytkownika: "
    printList userList

    let suma = sumList userList
    printf "\nSuma elementów w podanej liście: %d" suma


    match findMinMax userList with
        | Some(minVal, maxVal) -> printfn "\nMin: %d, max: %d" minVal maxVal
        | None -> printfn"\nLista jest pusta"
    0
    
