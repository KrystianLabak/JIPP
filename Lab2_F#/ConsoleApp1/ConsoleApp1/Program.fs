open System.IO
open System

//Napisz program, który pobiera tekst od użytkownika, a następnie oblicza i wyświetla:
//• Liczbę słów w podanym tekście.
//• Liczbę znaków (bez spacji).


//liczenie slow
let countWords(text: string) = 
    text.Split([|' '; '\t';'\n';';';':';'.'|], StringSplitOptions.RemoveEmptyEntries)
    |>Array.length

//liczenie znakow bez spacji
let countChars (text: string) =
    text.Replace(" ","").Length

printf "Podaj teskt: "
let inputText = Console.ReadLine()

let wordsCount = countWords inputText
let charCount = countChars inputText

printfn "Liczba słów: %d, a liczba znaków(bez spacji): %d" wordsCount charCount