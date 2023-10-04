import liarsDice as ld

def main():

    player1 = ld.Player("Dieter Ai", 1, True)
    player2 = ld.Player("Kevin Ai", 2, True)
    player3 = ld.Player("Adrian", 3, True)
    player4 = ld.Player("Fabi", 4, True)
    
    players = [player1, player2, player3, player4]

    win_count = {
        "Dieter Ai": 0,
        "Kevin Ai": 0,
        "Adrian": 0,
        "Fabi": 0
    }

    for i in range(1, 1001):
        player1 = ld.Player("Dieter Ai", 2, True)
        player2 = ld.Player("Kevin Ai", 1, True)
        player3 = ld.Player("Adrian", 3, True)
        player4 = ld.Player("Fabi", 4, True)

        players = [player1, player2, player3, player4]

        winner = ld.start_game(players, 1)
        win_count[winner.name] += 1
        print("Game: " + str(i))
    
    print(win_count)

main()