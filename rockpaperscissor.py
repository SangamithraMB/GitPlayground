def computer_winner(your_choice ,opponent_choice):
    print(f"You chose: {your_choice}")
    print(f"Opponent chose: {opponent_choice}")
    if your_choice == opponent_choice:
        return "It's a tie!"
    elif (your_choice == "rock" and opponent_choice == "scissors") or (your_choice == "scissors" and opponent_choice == "paper") or (your_choice == "paper" and opponent_choice == "rock"):
        return "You Win"
    else:
        return "You Lose"
your_input = input("Enter rock, paper or scissors: ").lower()
opponent_input = input("Enter opponent's choice (rock, paper or scissors): ").lower()
if your_input in ["rock","paper","scissors"] and opponent_input in ["rock","paper","scissors"]:
    result = computer_winner(your_input ,opponent_input)
    print(result)
else:
    print("Invalid input! Please enter rock, paper or scissors.")
