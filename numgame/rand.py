import random
N_DIG = 10
rand_dig = []


for i in range(N_DIG):
    rand_dig.append(random.randrange(N_DIG))

print(rand_dig)
