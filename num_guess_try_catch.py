#!/usr/bin/env python3
# created by: Sereke Asfeday
# Date: 15, October, 2026
# This program generates a random number between 1 and 9 then asks the user to guess.
# if tgey guessed correct it displays a message that they guessed correctly,
# if not it displays a message that they guessed incorrectly.

import random


def main():

    # generate a random number between 1 and 9
    random_number = int(random.randint(0, 9))

    try:
        # get user guess number as string between 0 and 9
        user_input = input("Enter your guess number between 0 and 9 : ")

        # here we tell the computer to convert or cast the string into an integer number.
        user_guess = int(user_input)

        # here we are telling the computer if the users guess equal to the random
        # display a message thats says they guessed correctly.
        if user_guess == random_number:
            print("You guessed correctly!\n")

        # and here if the user guess is not equal to random number
        # dispaly a messege thatthey guessed wrong. the correct guess was random number.
        else:
            print("Your guessed wrong. The correct guess was", random_number)
            print("\nGood Luck Next Time!")
    # here i wrote the exception message when the user types something else
    # it will display a message that tells the user the input is not valid integer.
    except Exception:
        print(user_input, "is not an integer number.")

    # here i wrote the finally block to display a final message after
    # the user guessed the number or typed something else.
    # the program ends it display Thank You for Playing!.
    finally:
        print("Thank You for Playing the Game!")


if __name__ == "__main__":
    main()
