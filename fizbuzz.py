import random

main_number = random.randint(1, 10)

try:
    user_input = int(input("Guess a number between 1 and 10: "))

    if user_input < 1 or user_input > 10:
        print("Please enter a number between 1 and 10.")

    elif user_input == main_number:
        print("Congratulations! You guessed correctly.")
        print("You were 100% correct!")

    else:
        difference = abs(main_number - user_input)
        percentage = ((9 - difference) / 9) * 100

        print(f"Correct number: {main_number}")
        print(f"You were {percentage:.2f}% correct.")

except ValueError:
    print("Please enter a valid integer.")