# HTML Generator with OpenAI API

## Opis aplikacji

Aplikacja służy do generowania kodu HTML na podstawie treści artykułu zapisanej w pliku tekstowym (`article.txt`). Kod HTML jest generowany przy użyciu API OpenAI i zapisuje artykuł w strukturze HTML zgodnej z najlepszymi praktykami. Użytkownik może wykorzystać ten kod w swoich projektach.

### Funkcje aplikacji:
1. **Odczyt pliku artykułu:** Aplikacja odczytuje treść pliku `article.txt`.
2. **Generowanie kodu HTML:** Za pomocą OpenAI API przekształca treść artykułu w strukturalny kod HTML.
3. **Zapis kodu HTML:** Wygenerowany kod HTML jest zapisywany w pliku `artykul.html`.
4. **Ustawienia środowiska:** Klucz API jest przechowywany w pliku `.env` dla większego bezpieczeństwa.

## Wymagania

- Python 3.10+
- Konto OpenAI i dostęp do klucza API
- Zainstalowane biblioteki z pliku `requirements.txt`

## Instrukcja uruchomienia

### 1. Klonowanie repozytorium
Sklonuj repozytorium na swój komputer:
```bash
git clone https://github.com/LukeLuterKing/Oxido.git
cd Oxido
```
### 2. Stwórz i aktywuj wirtualne środowisko (opcjonalne, ale zalecane):
```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```
### 3. Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```
### 4.Skonfiguruj klucz API OpenAI:

- Stwórz plik .env w głównym katalogu projektu.
- W pliku .env umieść klucz API w formacie:
```bash
OPENAI_API_KEY=your_openai_api_key
```
### 5. Uruchom program w terminalu

- Przykładowa treść artykułu znajduje się w pliku `article.txt`
- Wygenerowany kod HTML zostanie zapisany w pliku `artykul.html`.
```bash
python main.py
```