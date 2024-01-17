import random

def guess_the_number(x):

    print("====================")
    print("Welcome to the game!")
    print("====================")
    print(f"Select a number between 1 and {x} for the computer to try to guess it...")

    lower_limit = 1 
    upper_limit = x

    reply = ""
    while reply != "c":
        # Generate prediction
        if lower_limit != upper_limit:
            prediction = random.randint(lower_limit,upper_limit)
        else: 
            prediction = lower_limit #Could also be upper_limit

        # Get user feedback
        reply = input(f"My prediction is {prediction} If it is too high, enter (A). If very low, enter (B). If it is correct, enter (C): ").lower()

        if reply == "a":
            upper_limit = prediction - 1
        elif reply == "b":
            lower_limit = prediction + 1 

    print(f"Yeeeees!! The computer guessed your number correctly: {prediction}")      

guess_the_number(22)


