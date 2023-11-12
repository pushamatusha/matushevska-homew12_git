class Movie:
    def __init__(self, film_name, description, year, genres):
        self.film_name = film_name
        self.description = description
        self.year = year
        self.genres = genres
class FilmPlayer(Movie):
    def __init__(self, film_name, description, year, genres):
        super().__init__(film_name, description, year, genres)
        self.playing = False
        self.language = None
        self.recording = False

    def play(self):
        if not self.playing:
            if self.recording:
                print("Cannot play while recording. Stop recording first.")
            else:
                print(f"Playing film: {self.film_name} in {self.language} language")
                self.playing = True
        else:
            print("The film is already playing.")

    def choose_language(self, language):
        self.language = language
        print(f"Language set to {language}")

    def start_recording(self):
        if not self.recording:
            if self.playing:
                print("Cannot start recording while playing. Pause or stop playback first.")
            else:
                print("Recording started.")
                self.recording = True
        else:
            print("Recording is already in progress.")

    def stop_recording(self):
        if self.recording:
            print("Recording stopped.")
            self.recording = False
        else:
            print("Recording is not in progress.")

    def pause(self):
        if self.playing:
            print("Pausing the film.")
            self.playing = False
        else:
            print("The film is not playing.")

    def stop(self):
        if self.playing:
            print("Stopping the film.")
            self.playing = False
        else:
            print("The film is not playing.")

    def get_film_info(self):
        return self.film_name


film = FilmPlayer("Forrest Gump", "A man's journey through life", 1994, ["Drama"])
film.choose_language("English")
film.start_recording()
film.play()
film.pause()
film.stop_recording()
print(film.get_film_info())





