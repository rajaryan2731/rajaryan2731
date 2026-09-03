import random

def play_game():
    print("Welcome to Snake, Water, Gun Game!")
    options = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}

    while True:
        try:
            user_input = input("Enter 's' for Snake, 'w' for Water, 'g' for Gun (or 'q' to quit): ").lower()
        except EOFError:
            break

        if user_input == 'q':
            print("Thanks for playing!")
            break

        if user_input not in options:
            print("Invalid input. Please try again.")
            continue

        user_choice = options[user_input]
        comp_choice = random.choice(list(options.values()))

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            print("It's a tie!")
        elif (user_choice == 'Snake' and comp_choice == 'Water') or \
             (user_choice == 'Water' and comp_choice == 'Gun') or \
             (user_choice == 'Gun' and comp_choice == 'Snake'):
            print("You win!")
        else:
            print("You lose!")
        print("-" * 20)

if __name__ == "__main__":
    play_game()
