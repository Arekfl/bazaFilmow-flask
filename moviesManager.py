import sqlite3

def findMovie(search_string):
    """Wyszukuje filmy zawierające podany string w tytule lub aktorach."""
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    
    # Wyszukiwanie z użyciem LIKE (ignoruje wielkość liter)
    query = '''SELECT * FROM movies 
               WHERE title LIKE ? OR actors LIKE ?'''
    search_pattern = f'%{search_string}%'
    
    cursor.execute(query, (search_pattern, search_pattern))
    results = cursor.fetchall()
    
    if results:
        print(f'\nZnaleziono {len(results)} film(ów) dla "{search_string}":')
        for row in results:
            print(f'  - {row[1]}, ({row[2]}), {row[3]}')
    else:
        print(f'\nBrak filmów zawierających "{search_string}"')
    
    db.close()
    return results

# Przykłady użycia
if __name__ == '__main__':
    findMovie("Indi")
    findMovie("Connery")
    findMovie("Mat")
    findMovie("xxx")