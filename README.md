Dlaczego wybrano tokenizację słów

Wybór tokenizacji słów wynika z faktu, że wiele zastosowań NLP, takich jak analiza sentymentu,
klasyfikacja tekstu czy tłumaczenie maszynowe, wymaga analizy na poziomie słów. 
Tokenizacja słów pozwala na uchwycenie znaczenia i struktury języka w sposób bardziej granularny niż tokenizacja zdań czy znaków.

Implementacja Tokenizera

Implementacja tokenizera w Pythonie bez użycia wbudowanych bibliotek do tokenizacji wymaga kilku kroków:

Czyszczenie tekstu: Usunięcie niepotrzebnych znaków, takich jak interpunkcja, i konwersja tekstu do jednolitego formatu.

Podział na słowa: Dzielenie tekstu na słowa na podstawie białych znaków.

Obsługa wyjątków: Umożliwienie obsługi skrótów, liczb i innych wyjątków.

Opis implementacji

Funkcja clean_text:
Konwertuje tekst do małych liter, co zapewnia jednolitość.
Usuwa znaki interpunkcyjne, co pozwala na skupienie się na samych słowach.

Funkcja tokenize:
Najpierw czyści tekst za pomocą funkcji clean_text.
Następnie dzieli tekst na słowa na podstawie białych znaków.

Napotkane problemy i ich rozwiązania

Obsługa skrótów i liczb: Skróty takie jak "Dr." czy "U.S.A." oraz liczby mogą być problematyczne. Rozwiązanie to bardziej zaawansowane wyrażenia regularne lub dedykowane reguły do identyfikacji tych przypadków.

Znaki specjalne: Znaki specjalne jak myślniki w słowach złożonych mogą wymagać specjalnego traktowania. Można dodać wyjątki w wyrażeniach regularnych, aby zachować te znaki.

Język zależny: Tokenizer może wymagać dostosowania do specyficznych cech języka, takich jak odmiana wyrazów w języku polskim. Można to rozwiązać przez dodanie reguł specyficznych dla języka.