import random


def roll():
    die = random.randint(1, 6)
    return die


def roll2():
    die2 = random.randint(1, 6)
    return die2


summable = roll() + roll2()

if summable == 12:
    print('Great Job! You are perfect!')

elif summable >= 6 & summable < 12:
    print('Not Perfect but you could still win')

elif summable < 6:
    print('Better luck next time!')

print(summable)
