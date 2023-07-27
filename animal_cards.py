# animal_cards.py

"""
used this program to decide and test whether to use lists or dictionary
for the animal cards
"""

animals = ['cow', 'sheep', 'horse', 'chicken', 'pig', 'dog', 'cat',
           'duck', 'mouse', 'turkey']

card1 = ['cow', 'horse', 'pig', 'duck']

card2 = ['cow', 'sheep', 'dog', 'mouse']

card3 = ['horse', 'chicken', 'mouse', 'turkey']

card4 = ['sheep', 'pig', 'cat', 'turkey']

card5 = ['chicken', 'dog', 'cat', 'duck']

animal_dict = {'card1':['cow', 'horse', 'pig', 'duck'],
               'card2': ['cow', 'sheep', 'dog', 'mouse'],
               'card3': ['horse', 'chicken', 'mouse', 'turkey'],
               'card4': ['sheep', 'pig', 'cat', 'turkey'],
               'card5': ['chicken', 'dog', 'cat', 'duck']
               }

print(animal_dict)

print(animal_dict['card1'])
