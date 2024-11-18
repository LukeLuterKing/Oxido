from openai import OpenAI
from dotenv import load_dotenv
import os

#TODO STWORZYC PLIK README

# Wczytanie zmiennych środowiskowych z pliku .env
load_dotenv()

# Pobranie klucza API z pliku .env
api_key = os.getenv("OPENAI_API_KEY")

# Sprawdzenie, czy klucz API został poprawnie wczytany
if not api_key:
    raise ValueError("Brak klucza API. Ustaw zmienną OPENAI_API_KEY w pliku .env.")

# Inicjalizacja klienta OpenAI
client = OpenAI(api_key=api_key)

# Odczytanie pliku z artykułem
with open('article.txt', 'r', encoding='utf-8') as file:
    contents = file.read()

# Prompt do generowania HTML
prompt = (
    "Proszę wygenerować kod HTML dla artykułu, który spełnia poniższe wymagania:"
    "1. Struktura dokumentu:"
    "   - Tytuł artykułu powinien być otoczony tagiem <h1>."
    "   - Każda sekcja (tag <section>) artykułu powinna zawierać nagłówki <h2>, a podsekcje <h3>, zorganizowane w logiczny sposób."
    "   - Akapity treści otocz <p>."
    "   - Listy punktowane używaj z tagiem <ul>, a numerowane z <ol>."
    "2. Grafiki:"
    "   - W miejscach, gdzie artykuł wymaga uzupełnienia wizualnego, dodaj tag <img> z atrybutem src='image_placeholder.jpg'."
    "   - Każdy tag <img> powinien zawierać atrybut alt z pełnym opisem obrazu w języku polskim, zgodnym z treścią artykułu."
    "   - Każda grafika powinna być otoczona tagiem <figure>, a pod grafiką umieść podpis w tagu <figcaption>."
    "3. Dodatkowe wytyczne:"
    "   - Nie dołączaj żadnych znaczników formatowania, takich jak ```html, na początku ani na końcu wygenerowanego kodu."
    "   - Cały wygenerowany kod powinien być przeznaczony do wklejenia między znacznikami <body> i </body>."
    "   - Omiń nagłówki <html>, <head> oraz znacznik <body>."
    "4. Jakość kodu:"
    "   - Upewnij się, że kod jest czytelny, przejrzysty i dobrze sformatowany."
    "   - Struktura treści powinna być zgodna z zasadami semantyki HTML."
    "   - Kod musi być poprawny, gotowy do użycia i zgodny z najlepszymi praktykami HTML."
)

# Wysyłanie zapytania do OpenAI
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": f"{prompt} Artykuł:{contents}"
        }
    ]
)

# Pobranie wygenerowanego kodu HTML
page_summary = response.choices[0].message.content

# Zapisanie kodu do pliku HTML
output_file = "artykul.html"
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(page_summary)

print(f"Wygenerowany kod HTML zapisano w pliku {output_file}.")
