import os
import string
from titles import films_titles
from awards import films_awards
# крок 1
os.mkdir("Harry Potter")


for film in films_titles["results"]:
    film_title = film["title"].replace(":", "")
    film_dir = os.path.join("Harry Potter", film_title)
    os.mkdir(film_dir) # Папки з назв фільмів


# крок 2
for film in films_titles["results"]:
    film_title = film["title"].replace(":", "")
    film_dir = os.path.join("Harry Potter", film_title)

    for letter in string.ascii_uppercase:
        letter_dir = os.path.join(film_dir, letter)
        os.mkdir(letter_dir)


# крок 3 (тут в мене була помилка, в списку був тільки 1 фільм зі всіма нагородами, у колабі перевірила)
film_awards_list = []

for films in films_awards:
    for film_award in films['results']:
        award_info = {
            'award_name': film_award['award_name'],
            'award': film_award['award'],
            'type': film_award['type'],
            'title': film_award['movie']['title']
        }
        film_awards_list.append(award_info)

    for film_awards in film_awards_list:
        print(film_awards)

# крок 4
    sorted_film_awards = sorted(film_awards_list, key=lambda x: x['award_name'])

# крок 5
    for award_info in sorted_film_awards:
        award_name = award_info['award_name']
        award_letter = award_name[0].upper()

# а ось тут добавила цю точку касання, чому в мене всі файли додавались до всіх папок з літерами одразу
        for film in films_titles["results"]:
            if award_info['title'] == film['title']: # їх потрібно було порівняти за назвою
                film_title = film["title"].replace(":", "")
                film_dir = os.path.join("Harry Potter", film_title, award_letter)

                if os.path.exists(film_dir):
                    file_path = os.path.join(film_dir, f"{award_name}.txt")
                    with open(file_path, 'w') as award_file:
                        award_file.write(f"award name: {award_info['award_name']}\n")
                        award_file.write(f"award type: {award_info['type']}\n")
                        award_file.write(f"award: {award_info['award']}\n")
