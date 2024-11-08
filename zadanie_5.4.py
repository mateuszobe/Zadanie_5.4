import random
import datetime

#klasa bazowa - filmy:
class Film:
    def __init__(self, title, year, genre):
        self.title = title 
        self.year = year 
        self.genre = genre 
        self.views = 0

#funkcja zwiększająca liczbę odtworzeń:
    def play(self):
        self.views += 1
    
#funkcja wyświetlająca film jako string:
    def __str__(self):
        return f"{self.title} ({self.year})"

# klasa seriale dziedzicząca po filmach:  
class Serial(Film):
    def __init__(self, title, year, genre, season, episode):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode 

#funkcja wyświetlająca serial jako string:
    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d})"
    
#wspólna funkcja do filtrowania według typu (Film lub Serial):
def get_titles_by_type(library, title_type):
    return sorted([item for item in library if type(item) is title_type], key=lambda x: x.title)

#funkcja do filtrowania tylko filmów:
def get_movies(library):
    return get_titles_by_type(library, Film)

#funkcja do filtrowania tylko seriali:
def get_series(library):
    return get_titles_by_type(library, Serial)

#funkcja wyszukująca tytuł:
def search(library, title):
    return [item for item in library if title.lower() in item.title.lower()]

#funkcja losowo wybierająca element z biblioteki i dodająca mu losową ilość odtworzeń:
def generate_views(library):
    item = random.choice(library)
    item.views += random.randint(1, 100)

#funkcja uruchamiająca generate_views 10 razy:
def run_generate_views(library):
    for _ in range(10):
        generate_views(library)

#funkcja zwracająca wybrane najpopularniejsze tytuły z biblioteki:
def top_titles(library, top_n=3):
    return sorted(library, key=lambda x: x.views, reverse=True)[:top_n]

#program główny:
if __name__ == "__main__":
    library = [
        Film("Pulp Fiction", 1994, "Crime"),
        Film("The Matrix", 1999, "Sci-Fi"),
        Serial("The Simpsons", 1989, "Comedy", 1, 5),
        Serial("The Simpsons", 1989, "Comedy", 1, 6),
        Serial("Friends", 1994, "Comedy", 2, 10)
    ]
    print("Biblioteka filmów:")

    #generowanie losowych odtworzeń:
    run_generate_views(library)

    #wyświetlanie najpopularniejszych tytułów:
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    print(f"\nNajpopularniejsze filmy i seriale dnia {current_date}:")

    #top 3 najpopularniejszych tytułów:
    for title in top_titles(library):
        print(f"{title} - {title.views} odtworzeń")