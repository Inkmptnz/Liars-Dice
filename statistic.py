import math
import numpy
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

# print(binomial_distribution(15, 1, 1/6))
print(upper_cumulative_distribution(15,1, 1/6))
print(lower_cumulative_distribution(15,1, 1/6))

