from coin_strip import CoinStrip

# Game setup
num_coins = int(input("Enter number of coins: "))
strip = CoinStrip(num_coins)
strip.make()
strip.fill()
print("Starting Board:")
strip.show()

# Let's Play!
isPlayer1 = True
while True:
    # determine player move
    if isPlayer1:
        player = "Player 1"
        isPlayer1 = False
    else:
        player = "Player 2"
        isPlayer1 = True

    # get input
    move = input(f"{player} move: ")

    # exit game
    if move == "e" or move == "exit":
        break

    # move coin (assume player follows "num num" rule)
    move = move.split(" ")
    strip.move_coin(int(move[0]), int(move[1]))
    strip.show()

    # see if game is complete
    complete = strip.is_finished()
    if complete:
        print(f"{player} has won the game!\n")
        break
