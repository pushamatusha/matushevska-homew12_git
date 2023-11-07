# Крок 1 Перетворіть змінну ganres в словник.
import json
import os
import csv

from ganres import ganres
from films_data import films_data

genres_dict = json.loads(ganres)
print(genres_dict)

# Крок 2. Для кожного жанру у змінній ganres створіть окрему дерикторію.

new_direct = "Genres_dir"

if not os.path.exists(new_direct):
    os.mkdir(new_direct)

for genre in genres_dict["results"]:
    genre_name = genre["genre"]
    genre_dir = os.path.join(new_direct, genre_name)

    if not os.path.exists(genre_dir):
        os.mkdir(genre_dir)

# Крок 3. В кожній папці з жанром створіть CSV файл, він буде зберігати інформацію про фільми.

for genre in genres_dict["results"]:
    genre_name = genre["genre"]
    genre_dir = os.path.join("Genres_dir", genre_name)

    csv_file_path = os.path.join(genre_dir, "Info_film.csv")
    if not os.path.exists(csv_file_path):
        columns = ["title", "year", "rating", "type", "ganres"]

        with open(csv_file_path, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(columns)

# Крок 4. Відсортуй фільми у змінній films_data по жанрам. Тобто у файл csv з жанром запиши інформацію для кожнної колонки.

film_list = []  # список фільмів і жанрів до кожного(для себе)

for film in films_data:
    title = film['title']
    genres = [genre['genre'] for genre in film['gen']]

    film_list.append({'title': title, 'genres': genres})

for film in film_list:
    print(f"Title: {film['title']}, Genres: {', '.join(film['genres'])}")

for film in films_data:
    for genre_data in film['gen']:
        genre_name = genre_data['genre']
        csv_file_path = os.path.join("Genres_dir", genre_name, "Info_film.csv")

        with open(csv_file_path, 'a', newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([film["title"], film["year"], film["rating"], film["type"],';'.join(genre_data['genre'] for genre_data in film['gen'])])

