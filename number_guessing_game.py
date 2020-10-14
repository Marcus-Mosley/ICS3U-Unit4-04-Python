#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program is a Number Guessing Game with
#   Random Numbers and While True, Break


import random


def main():
    # This function creates a random number and checks if the user's guess
    #   is equal to the generated number

    # Input
    random_number = random.randint(0, 9)  # A number between 0 and 9

    while True:
        guess_str = input("Enter a number between 0 and 9: ")

        # Process & Output
        try:
            guess_int = int(guess_str)
        except Exception:
            print("That is not an integer, please input a number between 0 and"
                  " 9!")
            print("")
        else:
            if guess_int < 0 or guess_int > 9:
                print("You have not inputted a number between 0-9, please"
                      " input one in that range!")
                print("")
            else:
                if guess_int == random_number:
                    print("That is correct, the right number was {0}!"
                          .format(guess_int))
                    break
                else:
                    print("That is incorrect, please try again!")
                    print("")
    print("")
    print("Thanks for Playing!")


if __name__ == "__main__":
    main()
