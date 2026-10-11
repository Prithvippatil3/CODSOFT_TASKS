
import random


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"


def main():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("=" * 40)
    print("       ROCK PAPER SCISSORS")
    print("=" * 40)
    print("Rules: Rock beats Scissors")
    print("       Scissors beats Paper")
    print("       Paper beats Rock")
    print("Type 'quit' to exit the game.")

    while True:
        user = input(
            "\nEnter your choice (rock/paper/scissors): "
        ).strip().lower()

        if user == "quit":
            break

        if user not in choices:
            print("Invalid choice! Please try again.")
            continue

        computer = random.choice(choices)

        print("Your choice:     ", user)
        print("Computer's choice:", computer)

        winner = determine_winner(user, computer)

        if winner == "tie":
            print("Result: It's a tie!")
        elif winner == "user":
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            computer_score += 1

        print("-" * 40)
        print("Your score:", user_score)
        print("Computer score:", computer_score)
        print("-" * 40)

        while True:
            again = input("Play again? (yes/no): ").strip().lower()

            if again in ("yes", "y", "no", "n"):
                break

            print("Please enter yes or no.")

        if again in ("no", "n"):
            break

    print("\n========== FINAL SCORE ==========")
    print("Your score:    ", user_score)
    print("Computer score:", computer_score)

    if user_score > computer_score:
        print("Overall result: You won!")
    elif computer_score > user_score:
        print("Overall result: Computer won!")
    else:
        print("Overall result: It's a tie!")

    print("Thank you for playing!")


if __name__ == "__main__":
    main()
