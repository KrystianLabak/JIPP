//Stwórz funkcję, która sprawdza, czy podany ciąg znaków jest palindromem (czytany od przodu i od tyłu
//jest taki sam). Program powinien pobierać tekst od użytkownika i wyświetlać odpowiedni komunikat.

open System
open System.IO

let isPalindrom(text: string) =
    let clearText = text.Replace(" ","").ToLower()
    clearText = string(Array.rev(clearText.ToCharArray()))

//liczenie slow
let countWords(text: string) = 
    text.Split([|' '; '\t';'\n';';';':';'.'|], StringSplitOptions.RemoveEmptyEntries)
    |>Array.length

//liczenie znakow bez spacji
let countChars (text: string) =
    text.Replace(" ","").Length


[<EntryPoint>]
let main argv =
    
    printf "Podaj teskt: "
    let inputText = Console.ReadLine()

    let wordsCount = countWords inputText
    let charCount = countChars inputText

    printfn "Liczba słów: %d, a liczba znaków(bez spacji): %d" wordsCount charCount
    
    if isPalindrom inputText then
        printfn "Podany tekst jest palindromem"
    else
        printfn "Podany teskt nie jest palindromem"
    0