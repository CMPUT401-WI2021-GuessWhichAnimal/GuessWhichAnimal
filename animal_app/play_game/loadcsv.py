"""
To initialize animals into database:
0. Make sure this hasn't been done already
1. Make sure you have run migrations
2. python3 manage.py shell
3. from play_game.loadcsv import load_animals()
4. load_animals()
"""

from play_game.models import Animal
import csv

def load_animals():
    animals = []
    with open('../raw_data/wwf.csv', encoding='mac_roman') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        i = 0
        for row in reader:
            if i > 0: # Skip headers
                d = {}
                d['name'] = row[0]
                d['status'] = row[1]
                d['population'] = row[2]
                d['author'] = row[3]
                d['image_license'] = row[4]
                d['license_url'] = row[5]
                d['image_url'] = row[6]
                animals.append(d)
            i = 1

    for a in animals:
        entry = Animal(**a)
        entry.save()