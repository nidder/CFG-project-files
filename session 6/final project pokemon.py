
import random
import requests
import csv

def random_pokemon ():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        "move number": len(pokemon["moves"])
    }


def battle():
    player_name = input("Enter player name: ")

    my_pokemon = random_pokemon()
    opponent_pokemon = random_pokemon()

    #Player Pokemon description and stat choice.
    print("You got {}!" .format(my_pokemon["name"]))
    print("Here are {}'s stats:".format(my_pokemon["name"]))
    print("Id: {}" .format(my_pokemon["id"]))
    print("Height: {}".format(my_pokemon["height"]))
    print("Weight: {}".format(my_pokemon["weight"]))
    print("Move number: {}" .format((my_pokemon["move number"])))
    stat_choice = input("What stat do you want to use? id/height/weight/move number ")
    valid_inputs = ["id", "height", "weight", "move number"]

    #ERROR MESSAGE IF STAT INPUT IS INVALID
    def error():
        print("ERROR: Please enter your choice as 'id', 'height', or 'weight' (the field is case sensitive)")
        nonlocal stat_choice
        stat_choice = input("What stat do you want to use? id/height/weight ")

    while stat_choice not in valid_inputs:
        error()

    print("You chose **{}**! Time to battle!" .format(stat_choice))

    #BATTLE MECHANICS & RESULT
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    player_score = my_stat - opponent_stat
    print("Your opponent got {}!" .format(opponent_pokemon["name"]))
    print("The opposing {}'s {} is... {}!" .format(opponent_pokemon["name"], stat_choice, opponent_stat))

    if my_stat > opponent_stat:
        print("You win! Your score is {}." .format(player_score))

        new_score = "{} : {}".format(player_name, player_score)
        with open("playerscores.txt", "r") as text_file:
            text_scores = text_file.read()

        text_scores = text_scores + new_score + "\n"

        with open("playerscores.txt", "w+") as text_file:
            text_file.write(text_scores)

    if my_stat == opponent_stat:
        print("It's a draw!")
    if my_stat < opponent_stat:
        print("Your opponent wins!")

    print("Opponent's Pokemon stats are {}".format(opponent_pokemon))

    global play_again
    play_again = input("Play again? y/n:  ")

battle()

while play_again == "y":
    battle()








