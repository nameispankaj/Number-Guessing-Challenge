import random as r

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"You have selected the range ({start}, {end}).")

# Create a list with the numbers in the given range
given_range = list(range(start, end + 1))

print("\nGuess a number!")

failure = 0
while True:
    random_choice = r.choice(given_range)
    user_choice = int(input("Enter your choice: "))
    if user_choice not in given_range:
        print(f"Please choose a number within the given range ({start}, {end}).")
        failure += 1
    elif random_choice == user_choice:
        print("You guessed it right!")
        print(f"You failed {failure} times to achieve this victory!")
        break
    else:
        print(f"You selected {user_choice}, and the computer selected {random_choice}.")
        print("Game Over. Try again!")
        failure += 1
    print(f"\nYou have tried {failure} times.\n")
