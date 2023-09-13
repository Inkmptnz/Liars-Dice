import random

def probability(n):
    not_one = False
    j = 0
    count = 0
    while (not not_one):
        j += 1
        for i in range(n): 
            k = random.randint(1,6)
            if k == 1:
                count += 1
                if count == 6:
                    break
            if i == n - 1:
                not_one = True
        count = 0
    return j
        
def mult_prob(count, n):
    sum = 0
    for i in range(count):
        sum += probability(n)
    return sum / count

print(mult_prob(1000, 15))

def prob_min_one(dice_count):
    return 1 - pow((5/6), dice_count)

def prob_min_count(count, dice_count):
    return pow((1 - 1/count), dice_count)
