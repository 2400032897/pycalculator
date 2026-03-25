import random
players = ["Red","Blue"]
positions = {"Red": 0, "Blue": 0}
finish_line = 20
print("Welcome to Humanize Ludo!")
while True:
    for player in players:
        input(f"{player}'s turn. Press Enter to roll the dice...")
        dice_roll = random.randint(1, 6)
        print(f"{player} rolled a {dice_roll}!")
        positions[player] += dice_roll
        if positions[player] > finish_line:
            positions[player] = finish_line
        print(f"{player} is now at position {positions[player]}")
        
        if positions[player] >= finish_line:
            print(f"\n{player} wins the game! \nCongratulations!")
            exit(0) 