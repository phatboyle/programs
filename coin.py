import random
def coin():
    nside = random.randint(1,2)
    if nside==1:
        side = 'heads'
    else:
        side = 'tails'
    return side

side = coin()
print side
