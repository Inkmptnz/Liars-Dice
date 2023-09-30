import liarsDice as ld

def main():
    player1 = ld.Player("Dieter Ai", 1, True)
    player2 = ld.Player("Kevin Ai", 2, True)
    player3 = ld.Player("Adrian", 3, True)
    player4 = ld.Player("Fabi", 4, True)
        
    players = [player1, player2, player3, player4]

    ld.set_dices(players, 5)

    ld.start_game(players, 1)

main()