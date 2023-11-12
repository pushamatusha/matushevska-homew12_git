import os

os.mkdir('film_storage')

for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    letter_dir = os.path.join("film_storage", letter)
    if not os.path.exists(letter_dir):
        os.makedirs(letter_dir)
