import random

class Player:
    dices = []
    dice_count = 5
    bets = []

    def __init__(self, name, order):
        self.name = name
        self.order = order
    
    def __str__(self):
        return f"Name: {self.name}, Order: {self.order}, Dices: {str(self.dices)}, Dice count: {self.dice_count}"
    
    def __lt__(self, other):
        return self.order < other.order

def create_players(count):
    arr = []
    for i in range(count):
        player = Player(f"Player {i+1}", i + 1)
        arr.append(player)
    return arr

def set_dices(players, count_dices):
    for player in players:
        player.dices = random_dices(count_dices)
        player.dice_count = len(player.dices)

def random_dices(count_dices):
    return [random.randint(1,6) for _ in range(count_dices)]

def print_players(players):
    for player in players:
        print(player)

def count_dices(players):
    count_dices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for player in players:
        dices = player.dices
        if dices == []:
            continue
        for dice in dices:
            count_dices[dice] += 1
    return count_dices 

def get_dice_count_in_game(players):
    sum = 0
    for player in players:
        sum += player.dice_count 
    return sum

def start_game(players, player_count, start_dice_count, round):
    if len(players) == 1:
        print(f"\n--- {players[0].name} has won! ---")
        return
    
    print(f"--- Round {round} ---")
    if players == []:
        players = create_players(player_count)
        set_dices(players, start_dice_count)

    players.sort()
    print_players(players)
    called_liar = False
    i = 0
    first_bet = True
    last_bet = (-1,-1)
    bets = []
    while True:
        current_player = i%len(players)
        if (first_bet):
            last_bet = make_a_bet(players[current_player], dice_options(last_bet, get_dice_count_in_game(players)))
            players[current_player].bets.append(last_bet)
            bets.append(last_bet)
            first_bet = False
            i += 1
            continue
            
        print("The last bet was: ", last_bet[0], ", ", last_bet[1])

        while True:
            anwser = input("Do you call a lie? y/n \n")
            if anwser == "y":
                looser = called_a_liar(players[current_player - 1], players[current_player], count_dices(players))
                round_reset(looser, players, len(players), round)
                called_liar = True
                if len(players) > 1:
                    print_players(players)
                break
            elif anwser == "n":
                break
            else:
                print("You have to anwser either y or n")
        if called_liar:
            break

        last_bet = make_a_bet(players[current_player], dice_options(last_bet, get_dice_count_in_game(players)))
        players[current_player].bets.append(last_bet)
        bets.append(last_bet)
        i += 1

def round_reset(looser, players, player_count, round):
    beginning_looser_order = looser.order
    if looser.dice_count <= 0:
        players.remove(looser)
    for player in players:
        order = player.order
        player.order = ((order - beginning_looser_order) % len(players)) + 1
        player.dices = random_dices(player.dice_count)
    
    start_game(players, len(players), -1, round + 1)


def called_a_liar(accused, caller, count_dices):
    print(count_dices)
    accused_bet = accused.bets[-1]
    if count_dices[accused_bet[1]] >= accused_bet[0]:
        print("The accuser is WRONG! Wrong accusations lead to a loose of a dice.")
        caller.dice_count -= 1
        return caller
    else:
        print("He lied therefore he has to sacrifice a dice!")
        accused.dice_count -= 1
        return accused
    

def make_a_bet(current_player, dice_options):
    print(f"{current_player.name} make a bet!")
    while True:
        try:
            last_bet = tuple([int(x) for x in input("Make a bet with format: dice_count,dice\n").split(",")])
            if last_bet in dice_options:
                print("Your bet is: ", last_bet[0], ", ", last_bet[1])
                break
            print("Your Bet is not within the possibilities of the rule set. These are your current options: \n ", dice_options)
        except:
            print("The Input is invalid. Either you didn't used the comma incorrectly or you didnt give me two numbers. (Correct example: 1,2)")
    return last_bet
            

def dice_options(last_bet, dice_count_game):
    dice_permutation = []

    if last_bet == (-1,-1):
        for count in range(1, dice_count_game + 1):
            for dice in range(1, 7):
                dice_permutation.append((count, dice))
        return dice_permutation

    for dice in range(last_bet[1] + 1, 7):
        dice_permutation.append((last_bet[0], dice))

    for count in range(last_bet[0] + 1, dice_count_game + 1):
        for dice in range(1, 7):
            dice_permutation.append((count, dice))
    return dice_permutation

start_game([], 2, 1, 1)








