import random
from termcolor import colored

N_DIG = 10
rand_dig = []
rand_tmp = []
guess = []


def get_rand():
    for i in range(N_DIG):
        rand_dig.append(str(random.randrange(N_DIG)))
    
def get_guess():
    for i in range(N_DIG):
        d = input(f"Dig[{i}]: ")
        guess.append(d)

def print_list(list):
    for i in range(N_DIG):
        print(str(list[i]) + ':',end='') 
    print()

get_rand()
print(rand_dig)

get_guess()
print("comparing...")

rand_tmp = rand_dig; 
print("r: ",end='')
for i in range(N_DIG):
    print(rand_tmp[i] + ':', end='')
print()

print("g: ",end='')
for i in range(N_DIG):
    print(guess[i] + ':', end='')
print()

print('   ',end='')
for g in range(N_DIG):  # guess
    color = ''
    for r in range(N_DIG):  # rand
        rd = rand_tmp[r]
        gd = guess[g]
        if  rd == gd:
            if r == g:
                color = 'red'
                rand_tmp[r] = '.'
                break
            else:
                if not guess[r] == rand_tmp[r]:
                    color = 'blue'
                    rand_tmp[r] = '.'
                    break
    if color == '':
        color = 'green'                 
    print(colored(gd,color,attrs=['bold']) + ':', end='')
        
print()


    




