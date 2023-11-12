import os

print("Поточна директорія:", os.getcwd())
os.chdir("..")
os.chdir("FilmPlayer")
print("Поточна директорія:", os.getcwd())
class Film:
    def __init__(self, title, description, director, writer, cast, running_time, country, language, rating, year, budget, box_office, profitable, oscar_nominated, oscar_win, trailer):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.cast = cast
        self.running_time = running_time
        self.country = country
        self.language = language
        self.rating = rating
        self.year = year
        self.budget = budget
        self.box_office = box_office
        self.profitable = profitable
        self.oscar_nominated = oscar_nominated
        self.oscar_win = oscar_win
        self.trailer = trailer
        self.storage_address = self.generate_storage_address()
        self.create_storage_folders()
        self.upload_file()

    def get_film_info(self):
        info = f"Title: {self.title}\n"
        info += f"Description: {self.description}\n"
        info += f"Director: {', '.join(self.director)}\n"
        info += f"Writer: {self.writer}\n"
        info += f"Cast(actors): {', '.join(self.cast)}\n"
        info += f"Running time: {self.running_time} minutes\n"
        info += f"Country: {self.country}\n"
        info += f"Language: {self.language}\n"
        info += f"IMDb RATING: {self.rating}\n"
        info += f"Year: {self.year}\n"
        info += f"Budget: {self.budget}\n"
        info += f"Box office: {self.box_office}\n"
        info += f"Profitable: {self.profitable}\n"
        info += f"Oscar nominated: {self.oscar_nominated}\n"
        info += f"Oscar win: {self.oscar_win}\n"
        info += f"Trailer: {self.trailer}"
        return info

    def generate_storage_address(self):
        first_letter = self.title[0].upper()
        filename = self.title.replace(" ", "_") + ".txt"
        return os.path.join("film_storage", first_letter, filename)

    def create_storage_folders(self):
        storage_folder = os.path.join("film_storage")
        if not os.path.exists(storage_folder):
            os.mkdir(storage_folder)
        first_letter_folder = os.path.join(storage_folder, self.title[0].upper())
        if not os.path.exists(first_letter_folder):
            os.mkdir(first_letter_folder)

    def upload_file(self):
        with open(self.storage_address, "w") as file:
            file.write(self.get_film_info())

    def get_film_address(self):
        return self.storage_address

film_info = [
    "Crazy, Stupid, Love",
    "A middle-aged husband's life changes dramatically when his wife asks him for a divorce...",
    ["Glenn Ficarra", "John Requa"],
    "Dan Fogelman",
    ["Steve Carell", "Ryan Gosling", "Julianne Moore"],
    118,
    "United States",
    "English",
    7.4,
    2011,
    "$50 million",
    "$145 million",
    "Yes",
    "No",
    "No",
    "https://www.imdb.com/video/vi3722091801/"
]
crazy_stupid_love = Film(*film_info)






