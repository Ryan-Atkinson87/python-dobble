# dobble.py

"""
Dobble game where a player is shown two sets (cards) of animal
names and the player has to say which animal is the same in each set (card)
A single animal only appears on 2 different cards
Player can have a timer to let them know how fast they inputted the matching animal
"""

from random import *

animal_dict = {'Card 1':['cow', 'horse', 'pig', 'duck'],
               'Card 2': ['cow', 'sheep', 'dog', 'mouse'],
               'Card 3': ['horse', 'chicken', 'mouse', 'turkey'],
               'Card 4': ['sheep', 'pig', 'cat', 'turkey'],
               'Card 5': ['chicken', 'dog', 'cat', 'duck']
               }

instructions = 'You will be shown two different cards, the cards contain a single matching pair of animals. Type which pair you think are matching'



    

print(instructions)
exit = False

while not exit:
    user_input = input('Type "yes" to play, "no" to exit or "i" to see the instructions again: ')
    if user_input == 'yes' or user_input == 'Yes':
        # select 2 random keys from animal_dict
        keys_list = list(animal_dict)
        counter = 2
        temp_lst = []
        while counter > 0:
            rand_key = choice(keys_list)
            if rand_key in temp_lst:
                counter = counter
            else:
                temp_lst = temp_lst + [rand_key]
                counter = counter -1

        # add the values of the 2 random keys from animal_dict to rand_dict
        rand_card1 = temp_lst[0]
        rand_card2 = temp_lst[1]
        rand_dict = {}
        rand_dict[rand_card1] = animal_dict[rand_card1]
        rand_dict[rand_card2] = animal_dict[rand_card2]

        # prints the 2 random cards on seperate lines
        line1 = ''
        for item in rand_dict[rand_card1]:
            line1 = line1 + ' ' + item
        print(rand_card1 + ':' + line1)
        line2 = ''
        for item in rand_dict[rand_card2]:
            line2 = line2 + ' ' + item
        print(rand_card2 + ':' + line2)


        # check which animal matches
        # start timer
        answer = input('Which is the matching animal?: ')
    elif user_input == 'no' or user_input == 'No':
        exit = True
    elif user_input == 'i' or user_input == 'I':
        print(instructions)
    else:
        print('You need to type "yes", "no" or "i"')


