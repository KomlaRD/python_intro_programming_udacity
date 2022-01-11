import time
import random

items = []
enemies = ["Lion", "Witch", "Tiger", "Shark", "Dragon"]
weapons = ["Gun", "Sword", "Bow and Arrow", "Dagger"]

enemy = random.choice(enemies)
weapon = random.choice(weapons)



def print_pause(string):
    print(string)
    time.sleep(3)


def intro():

    print_pause("You find yourself standing in an open field" + " " +
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a" + " " + enemy + " " + "is somewhere"
                + " " + "around here and has been terrifying" + " " +
                "the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty" + " " +
                "(but not effective) dagger.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

def game_input():
    choice = input("(Please enter 1 or 2).")


def game_choice():
    if "1" in choice:
        house()
        fight(items)
    elif "2" in choice:
        cave()
        field()
    else:
        print_pause("Try again! (Please enter 1 or 2).")
        do_what()


def play_again():
    again = input("Would you like to play again? (y/n)")
    if "y" in again:
        print_pause("Excellent, welcome back!")
        intro()
        game_input()
        game_choice()
    elif "n" in again:
        print_pause("See you next time!")
        return None
    else:
        print_pause("Please enter y/n")


def house():

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens" + " " +
                "and out steps a" + " " + enemy)
    print_pause("Eep! This is the" + " " + enemy + "'s" + " " + "house!")
    print_pause("The" + " " + enemy + " " + "attacks you!")
    print_pause("You feel a bit under-prepared for this" + " " +
                "what with only having a tiny dagger.")


def cave():

    print_pause("You peer cautiosly into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical" + " " + weapon + "!")
    print_pause("You discard your silly old dagger and" + " " +
                "take the" + " " + weapon + " " + "with you.")
    items.append(weapon)


def field():

    print_pause("You walk back to the field")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    field_again()



def field_again():
    choice_field = input("(Please enter 1 or 2).")
    if "1" in choice_field:
        house()
        fight(items)
    elif "2" in choice_field:
        cave()
        do_what()
        game_choice()
    else:
        game_input()


def fight(items):
    choice_fight = input("Would you like to (1) fight or (2) run away?")
    if choice_fight == "1":
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the" + " " + enemy)
        print_pause("You have been defeated!")
        weapon_change(items)
    elif "2" in choice_fight:
        field()
        do_what()
        choice_again = input("(Please enter 1 or 2).")
        if "1" in choice_again:
            house()
        elif "2" in choice_again:
            cave()
            do_what()
    else:
        choice_fight = input("Would you like to (1) fight or (2) run away?")


def weapon_change(items):
    if weapon in items:
        print_pause("As the" + " " + enemy + " " + "moves to attack," + " " +
                    "you remove your new" + " " + weapon)
        print_pause("But the" + " " + enemy + " " + "takes one look at your"
                    + " " + "shiny new toy and runs away!")
        print_pause("You have rid the town of the" + " " + enemy + " " +
                    "You are victorious!")


def do_what():
    print_pause("What would you like to do?")
    game_input()


intro()
choice = input("(Please enter 1 or 2).")
game_choice()
play_again()
