import random

class Player:
    current_dices = []
    current_dice_count = 5

    def __init__(self, name, order):
        self.name = name
        self.order = order
    
    def __str__(self):
        return f"Name: {self.name}, Order: {self.order}, Dices: {str(self.current_dices)}"
    
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
        player.current_dices = random_dices(count_dices)

def random_dices(count_dices):
    return [random.randint(1,6) for _ in range(count_dices)]

def print_player(player):
    for i in player:
        print(i)

def count_dices(players):
    count_dices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for player in players:
        dices = player.current_dices
        if dices == []:
            continue
        for dice in dices:
            count_dices[dice] += 1
    return count_dices 

def start_game(player_count, start_dice_count):
    players = create_players(player_count)
    set_dices(players, start_dice_count)
    sorted(players)

    rounds = []
    no_liar = True
    i = 0
    first_bet = True
    while no_liar:
        if (first_bet):
            print(dice_options(-1, player_count, start_dice_count))

def dice_options(last_bet, player_count, start_dice_count):
    dice_permutation = []
    if last_bet == -1:
        for times in range(player_count*start_dice_count + 1):
            for dice in range(6):
                dice_permutation.append((times, dice))
    return dice_permutation

print(dice_options(-1, 4, 5))