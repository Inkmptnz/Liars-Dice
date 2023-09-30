import math

# n tries, k success count, p success chance
def binomial_distribution(n, k, p):
    return binomial_coefficient(n, k) * pow(p, k) * pow(1-p, n-k)

def binomial_coefficient(n, k):
    product = 1
    for i in range(1, k + 1):
        product *= (n + 1 - i) / i
    return product

def upper_cumulative_distribution(n, k, p):
    sum = 0
    for i in range(math.floor(k), n + 1):
        sum += binomial_distribution(n, i, p)
    return sum

def lower_cumulative_distribution(n, k, p):
    sum = 0
    for i in range(0, math.floor(k) + 1):
        sum += binomial_distribution(n, i, p)
    return sum

def probability_bet_correct(count_visible_face, count_bet, remaining_dices):
    return upper_cumulative_distribution(remaining_dices, count_bet - count_visible_face, 1/6)

def sigma(n, p, k):
    sigma = math.sqrt(n * p * (1-p))
    return sigma * k

def ai_handler(want_lie, last_bet, ai, players, increase_count_pow, change_count_new_face_pow):
    if want_lie:
        return is_ai_calling_lie(last_bet, ai, players, increase_count_pow)
    else:
        return ai_bet_decision(last_bet, ai, players, increase_count_pow, change_count_new_face_pow)
    
def is_ai_calling_lie(last_bet, ai, players, increase_count_pow):
    from liarsDice import get_dice_count_ingame, count_dices
    face = last_bet[1]
    dice_count = last_bet[0]

    dict_dices = count_dices([ai])
    dice_count_ingame = get_dice_count_ingame(players)
    
    if (last_bet == (-1, -1)):
        return False
    # when probability if dice count is lower than roughly 5%
    # 3 3 4 6 6
    # 6 3
    # 6 - 2 > (20 - 5) / 6 + sigma((20 - 5), 1/6, 1,64)
    dice_count_diff = dice_count_ingame - dice_count
    if ((dice_count - dict_dices[face]) > dice_count_diff/6 + sigma(dice_count_diff, 1/6, 1.64)):
        return True

    return False
    

def ai_bet_decision(last_bet, ai, players, increase_count_pow, change_count_new_face_pow):
    from liarsDice import get_dice_count_ingame, count_dices

    dice_count = last_bet[0]
    face = last_bet[1]

    dice_count_ingame = get_dice_count_ingame(players)
    bet_count_porpotion =  dice_count / dice_count_ingame

    ai_face = face
    ai_count = dice_count + 1
    dict_dices = count_dices([ai])

    
    if (last_bet == (-1, -1)):
        ai_face = highest_dice_count(dict_dices)
        ai_count = dict_dices[ai_face]
        return (ai_count, ai_face)
    
    # 3 3 4 6 6
    # 3 3
    # 3 + 2 * (1 - 3/20)
    # 8 + 1 * (1 - 8/20) = 8.6 = 9
    # 8 + 1 * (1 - 8/20)^1,5 = 8.6 = 9
    if (face in ai.dices):
        ai_count  = dice_count + round(dict_dices[face] * pow((1 - bet_count_porpotion), increase_count_pow))
    else:
        ai_count = dice_count + round(dict_dices[face] * pow((1 - bet_count_porpotion), change_count_new_face_pow))
        if ai_count == dice_count:
            ai_count += 1
        ai_face = highest_dice_count(dict_dices)
    
    ai_bet = (ai_count, ai_face)
    return ai_bet



# highest face is prioritized
def highest_dice_count(dict_dices):
    max_face = max(dict_dices, key=dict_dices.get)
    for face in dict_dices:
        if (dict_dices[face] == dict_dices[max_face] and face > max_face):
            max_face = face

    return max_face