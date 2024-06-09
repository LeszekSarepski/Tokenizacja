import re

class Tokenizer:
    def __init__(self):
        pass

    def clean_text(self, text):
        # Konwersja do małych liter
        text = text.lower()
        # Usuwanie znaków interpunkcyjnych
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def tokenize(self, text):
        # Czyszczenie tekstu
        clean_text = self.clean_text(text)
        # Podział na słowa
        tokens = clean_text.split()
        return tokens

# Przykładowe użycie
tokenizer = Tokenizer()
text = "To jest przykładowy tekst, który będzie tokenizowany!"
tokens = tokenizer.tokenize(text)
print(tokens)
