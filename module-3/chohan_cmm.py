# chohan_cmm.py
# Modified by: Cameron Mendez
# CSD-325 Module 3 - Cho-Han Game with Bonus Rule

import random

def main():
    purse = 5000
    print("Welcome to Cho-Han!")
    print("Try your luck betting on whether the dice sum is even or odd.")
    print("If the dice total is a 2 or a 7, you receive a 10 mon bonus!")  # <-- Added bonus rule to intro

    # Main game loop
    while purse > 0:
        print("\nYou have", purse, "mon.")
        bet = int(input("crm: "))  		# <-- Changed prompt to initials

        if bet > purse or bet <= 0:
            print("Invalid bet.")
            continue

        choice = input("Cho (even) or Han (odd)? ").lower()
        if choice not in ["cho", "han"]:
            print("Invalid choice.")
            continue

        # Dice roll
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"The dealer rolls {die1} and {die2}. Total is {total}.")

        result = "cho" if total % 2 == 0 else "han"

        # Bonus Rule
        if total == 2 or total == 7:
            print("Bonus! You rolled a", total, "— you earn a 10 mon bonus!")  # <-- Bonus message
            purse += 10  # <-- Added 10 mon to purse

        if choice == result:
            winnings = bet
            house_cut = int(winnings * 0.12)  # <-- Changed house cut to 12%
            winnings -= house_cut
            print("You win! House takes", house_cut, "mon. You gain", winnings, "mon.")
            purse += winnings
        else:
            print("You lose!")
            purse -= bet

    print("You're out of money. Game over!")

# Run the program
main()
