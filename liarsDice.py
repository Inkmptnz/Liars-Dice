import random

class Player:
    current_dices = []
    current_dice_count = 5
    bets = []

    def __init__(self, name, order):
        self.name = name
        self.order = order
    
    def __str__(self):
        return f"Name: {self.name}, Order: {self.order}, Dices: {str(self.current_dices)}, Dice count: {self.current_dice_count}"
    
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

def print_players(players):
    for player in players:
        print(player)

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
    
    called_liar = False
    i = 0
    first_bet = True
    last_bet = (-1,-1)
    bets = []
    while True:
        current_player = i%player_count
        print(players[current_player])
        if (first_bet):
            last_bet = make_a_bet()
            players[current_player].bets.append(last_bet)
            bets.append(last_bet)
            first_bet = False
            i += 1
            continue
            
        print("The last bet was: ", last_bet[0], ", ", last_bet[1])

        while True:
            anwser = input("Do you call a lie? y/n \n")
            if anwser == "y":
                called_a_liar(players[current_player - 1], players[current_player], count_dices(players))
                called_liar = True
                print_players(players)
                break
            elif anwser == "n":
                break
            else:
                print("You have to anwser either y or n")
        if called_liar:
            break

        last_bet = make_a_bet()
        players[current_player].bets.append(last_bet)
        bets.append(last_bet)
        i += 1
        
def called_a_liar(accused, caller, count_dices):
    print(count_dices)
    accused_bet = accused.bets[-1]
    if count_dices[accused_bet[1]] >= accused_bet[0]:
        print("The accuser is WRONG! Wrong accusations lead to a loose of a dice.")
        caller.current_dice_count -= 1
    else:
        print("He lied therefore he has to sacrifice a dice!")
        accused.current_dice_count -= 1
    

def make_a_bet():
    last_bet = (-1, -1)
    while True:
        try:
            last_bet = [int(x) for x in input("Make a bet with format: dice_count,dice\n").split(",")]
            print("Your bet is: ", last_bet[0], ", ", last_bet[1])
            break
        except:
            print("The Input is invalid. Either you didn't used the comma incorrectly or you didnt give me two numbers. (Correct example: 1,2)")
    return last_bet
            

def dice_options(last_bet, player_count, start_dice_count):
    dice_permutation = []
    if last_bet == (-1,-1):
        for count in range(1, player_count*start_dice_count + 1):
            for dice in range(1, 7):
                dice_permutation.append((count, dice))
        return dice_permutation

    for dice in range(last_bet[1] + 1, 7):
        dice_permutation.append((last_bet[0], dice))

    for count in range(last_bet[0] + 1, player_count*start_dice_count):
        for dice in range(1, 6):
            dice_permutation.append((count, dice))
    return dice_permutation

start_game(4,5)







