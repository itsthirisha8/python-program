import random

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing!")
        return  # Base case: stop recursion
    
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        return play_game()  # Recursive call for invalid input
    
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
    print()
    
    play_game()  # Recursive call to play again

# Start the game
play_game()

