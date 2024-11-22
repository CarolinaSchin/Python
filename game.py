import random
import time


def print_pause(message, pause):
    print(message)
    time.sleep(pause)


def intro():
    print_pause("You find yourself lost in an open field, "
                "filled with grass and yellow wildflowers.", 2)
    print_pause(f"Rumor has it that a {creature} "
                "is somewhere around here.", 2)
    print_pause(f"The {creature} is the only one who possesses"
                " the map to leave the forest and return to the city.", 2)
    print_pause(f"You have a small {weapon} for your safeguarding.", 2)
    print_pause("You can see a huge castle in front of you"
                " and a trail on your right.", 2)


def to_go():
    print_pause("Enter 1 to knock on the door of the castle.", 2)
    print_pause("Enter 2 to follow the trail.", 2)
    print_pause("What would you like to do?", 2)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
    if choice == "1":
        castle()
    elif choice == "2":
        trail()


def castle():
    print_pause(f"You are in front of the door of the castle,"
                f" you knock on the door and a {creature} greets you.", 2)
    print_pause("You are in serious dangerous!", 2)
    print_pause(f"This is the magical {creature}'s house!", 2)
    fight(weapon)


def fight(weapon):
    print_pause(f"The {creature} attacks you.", 2)
    if weapon == "pocket knife":
        print_pause(f"The creature is too strong and"
                    f" you just have your {weapon}.", 2)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("Would you like to (1) fight or (2) run away?\n")
    if choice == '1':
        if weapon == "pocket knife":
            print_pause("You do your best.", 2)
            print_pause(f"Your {weapon} is not strong enough.", 2)
            print_pause("You are now trapped into de castle.", 2)
            print_pause("You are defeated!", 2)
        elif weapon == "magic sword":
            print_pause(f"The {creature} attacks you.", 2)
            print_pause("The magic sword is in your hand"
                        " and you brace yourself for the attack.", 2)
            print_pause("You find the map and go back home."
                        " You are victorious!", 2)
    elif choice == '2':
        print_pause("You run back into the field."
                    " Luckily, you don't seem to have been followed.", 2)
        to_go()


def trail():
    global visiting_trail_first_time
    global weapon
    if visiting_trail_first_time:
        print_pause("You follow de trail carefully.", 2)
        print_pause("Soon you meet a kind fairy protecting a magic sword.", 2)
        print_pause("You tell her you need a map to go back home.", 2)
        print_pause(f"She tells you the map is in the castle"
                    f" and gives you a magic sword to face the {creature}.", 2)
        print_pause("You walk back out of the fiels.", 2)
        weapon = "magic sword"
        visiting_trail_first_time = False
    else:
        print_pause("You've been here before, and gotten the magic sword.", 2)
    to_go()


def again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)\n")
    if choice == 'n':
        print_pause("Thanks for playing! See you next time.", 2)
        return 'game_over'
    elif choice == 'y':
        print_pause("Excellent! Restarting the game ...", 2)
        weapon = "pocket knife"
        return 'running'


if __name__ == "__main__":
    game_status = 'running'
    while game_status == 'running':

        magic_creature = ['goblin', 'werewolf', 'troll', 'basilisk', 'golem']
        creature = random.choice(magic_creature)
        weapon = 'pocket knife'
        visiting_trail_first_time = True

        intro()
        to_go()

        game_status = again()
