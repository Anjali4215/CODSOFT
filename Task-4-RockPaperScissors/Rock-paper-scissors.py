import random

def play_game():
    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("Instructions: Type rock, paper, or scissors to play.\n")

    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("👉 Enter your choice (rock/paper/scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("❌ Invalid choice! Please enter rock, paper, or scissors: ").lower()

        # Computer choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Show choices
        print(f"\n✅ You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        # Game logic
        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😢 Computer wins this round!")
            computer_score += 1

        # Show score
        print(f"\n📊 Score -> You: {user_score} | Computer: {computer_score}")

        # Ask to play again
        play_again = input("\n🔄 Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n👋 Thanks for playing Rock-Paper-Scissors!")
            print(f"🏆 Final Score -> You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🎊 Congratulations! You are the overall winner!")
            elif computer_score > user_score:
                print("💻 Computer wins overall! Better luck next time!")
            else:
                print("🤝 It's an overall tie!")
            break


# Run the game
play_game()
