# Baza Filmów

Aplikacja webowa do zarządzania bazą danych filmów, zbudowana przy użyciu Flask i SQLite.

## Funkcjonalności

- Wyświetlanie listy filmów
- Dodawanie nowych filmów (tytuł, rok produkcji, aktorzy)
- Usuwanie filmów z bazy danych

## Wymagania

- Python 3.8+
- Flask 3.0.0

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/Arekfl/bazaFilmow-flask.git
cd bazaFilmow-flask
```

2. Utwórz wirtualne środowisko (opcjonalne)

3. Zainstaluj wymagane pakiety / requirements.txt

## Uruchomienie

1. Upewnij się, że jesteś w katalogu projektu: cd bazaFilmow-flask

2. Uruchom aplikację: python app.py


3. Otwórz przeglądarkę i przejdź do: http://127.0.0.1:5000

## Struktura projektu

```
bazaFilmow-flask/
├── app.py              # Główna aplikacja Flask
├── movies.db           # Baza danych SQLite
├── requirements.txt    # Zależności projektu
├── static/
│   ├── script.js      # Skrypty JavaScript
│   └── styles.css     # Style CSS
└── templates/
    ├── Index.html     # Strona główna
    └── add.html       # Formularz dodawania filmu
```

## Technologie

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Baza danych**: SQLite
