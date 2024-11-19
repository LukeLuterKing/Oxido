from openai import OpenAI
from dotenv import load_dotenv
import os


def load_api_key():
    """
    Wczytuje klucz API z pliku .env.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Brak klucza API. Ustaw zmienną OPENAI_API_KEY w pliku .env.")
    return api_key


def read_article(file_path):
    """
    Wczytuje treść artykułu z podanego pliku.

    :param file_path: Ścieżka do pliku tekstowego z artykułem.
    :return: Zawartość pliku jako string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def generate_html(api_key, article_content):
    """
    Wysyła zapytanie do API OpenAI w celu wygenerowania kodu HTML dla artykułu.

    :param api_key: Klucz API OpenAI.
    :param article_content: Treść artykułu jako string.
    :return: Wygenerowany kod HTML.
    """
    client = OpenAI(api_key=api_key)

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

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": f"{prompt} Artykuł:{article_content}"
            }
        ]
    )

    return response.choices[0].message.content


def save_html_to_file(html_content, output_file):
    """
    Zapisuje wygenerowany kod HTML do pliku.

    :param html_content: Kod HTML jako string.
    :param output_file: Ścieżka do pliku wyjściowego.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Wygenerowany kod HTML zapisano w pliku {output_file}.")


def main():
    """
    Główna funkcja programu.
    """
    try:
        api_key = load_api_key()
        article_content = read_article('article.txt')
        html_content = generate_html(api_key, article_content)
        save_html_to_file(html_content, "artykul.html")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    main()
