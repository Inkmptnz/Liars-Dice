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

def auto_create_player(player_count, start_dice_count):
    players = create_players(player_count)
    set_dices(players, start_dice_count)
    return players

def start_game(players, round):
    if len(players) == 1:
        print(f"\n--- {players[0].name} has won! ---")
        return
    
    players.sort()

    print(f"--- Round {round} ---")
    print_players(players)

    i = 0
    first_bet = True
    last_bet = (-1,-1)

    while True:
        current_player_index = i%len(players)
        current_player = players[current_player_index]

        if not first_bet and is_player_calling_lie(players, current_player_index) :
            looser = who_is_looser(players[current_player_index - 1], players[current_player_index], count_dices(players))
            looser.dice_count -= 1
            round_reset(looser, players, round)
            break
        
        last_bet = make_a_bet(last_bet, current_player, get_dice_count_in_game(players))
        current_player.bets.append(last_bet)
        i += 1
            
        print("The last bet was: ", last_bet[0], ", ", last_bet[1])

        first_bet = False

def is_player_calling_lie(players, current_player_index):
    while True:
        anwser = input("Do you call a lie? y/n \n")
        if anwser == "y":
            return True
        elif anwser == "n":
            return False
        else:
            print("You have to anwser either y or n")

def round_reset(looser, players, round):
    beginning_looser_order = looser.order

    if looser.dice_count <= 0:
        players.remove(looser)
    
    for player in players:
        order = player.order
        player.order = ((order - beginning_looser_order) % len(players)) + 1
        player.dices = random_dices(player.dice_count)

    start_game(players, round + 1)


def who_is_looser(accused, caller, count_dices):
    print(count_dices)
    accused_bet = accused.bets[-1]

    if count_dices[accused_bet[1]] >= accused_bet[0]:
        print("The accuser is WRONG! Wrong accusations leads to a lost dice.")
        return caller
    else:
        print("He lied therefore he has to sacrifice a dice!")
        return accused
    

def make_a_bet(last_bet, current_player, dice_count_game):
    is_first_bet = last_bet == (-1,-1)
    print(f"{current_player.name} make a bet!")
    while True:
        try:
            current_bet = tuple([int(x) for x in input("Make a bet with format: dice_count,dice\n").split(",")])
            if is_first_bet:
                if does_bet_exist(current_bet, dice_count_game):
                    print("Your bet is: ", current_bet[0], ", ", current_bet[1])
                    return current_bet
                continue

            if does_bet_exist(current_bet, dice_count_game) and is_bet_possible(last_bet, current_bet, dice_count_game):
                print("Your bet is: ", current_bet[0], ", ", current_bet[1])
                return current_bet

        except:
            print("The Input is invalid. Either you didn't used the comma incorrectly or you didnt give me two numbers. (Correct example: 1,2)")

def does_bet_exist(bet, dice_count_game):
    if bet[1] < 1 or bet[1] > 6:
        print("Your dice doesn't exist.")
        return False
    
    if bet[0] < 1 or bet[0] > dice_count_game:
        print("There aren't even enough dice for your count.")
        return False
    
    return True

def is_bet_possible(last_bet, new_bet, dice_count_game):
    if last_bet > new_bet:
        print("Your bet is not within the possibilities of the rule set. These are your current options: \n", dice_options(last_bet, dice_count_game))
        return False
    
    return True

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

def main():
    players = auto_create_player(2,1)
    start_game(players, 1)

main()