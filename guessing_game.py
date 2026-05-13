import random


while True:
    print("=" * 30)
    print("   GUESS THE NUMBER")
    print("   Guess the number from 1 to 100")
    print("   Choose difficulty level")
    print("   1. Easy  (10 guesses)")
    print("   2. Medium  (7 guesses)")
    print("   3. Hard  (5 guesses)")
    print("=" * 30)

    choice = int(input("select 1,2, or 3: "))
    if choice == 1:
        limit = 10
    elif choice == 2:
        limit = 7
    else:
        limit = 5

    print(f"Alright, try and guess the number from 1 to 100. You have {limit} guesses left.")
    print("=" * 30)

    number = random.randint(1, 100)
    attempts = 0
    guess = None 
    first_guess = True


    while attempts < limit:
        if first_guess:
            guess = int(input("Guess your number: "))
            first_guess = False
        else:
            guess = int(input("Guess your number again einstein: "))
        attempts = attempts + 1

        if number == guess:
            print("Yeah whatever you guessed the number.")
            break

        if number > guess:
            print(f"Too afraid to guess wrong? Go higher. ({limit - attempts}) guesses left.")
        else:
            print(f"Oh, going too high, are we? ({limit - attempts} attempts left)")

    if number != guess and attempts == limit:
        print(f"Good job. You are out of guesses. Was {number} too tough to guess? Now go stand in the corner.")

    while True:
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again == "yes":
            break
        elif again == "no":
            print("Goodbye.")
            exit()
        else:
            print("Invalid input. Type yes or no, albert einstein.")
