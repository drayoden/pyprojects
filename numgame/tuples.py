# colors: R, G, B, W

guess_list = []
guess = [(2,'R'),(9,'W'),(4,'G')]

print(guess)

for d,c in guess:
    print(f"[{d}] --> [{c}]")

for x in guess:
    print(x)

print("adding to guess_list...")

guess_list.append(guess)
print(guess_list)

new_guess = [(4,'B'),(7,'G'),(1,'B')]
guess_list.append(new_guess)

print(guess_list)
print(len(guess_list))

new_guess = [(9,'B'),(3,'G'),(2,'W')]
guess_list.append(new_guess)

print(guess_list)
print(len(guess_list))

# list of guesses...
for i in range(len(guess_list)):
    print(guess_list[i])

# iterate all of the guesses lists...
for i in range(len(guess_list)):
    for j in range(len(guess_list[i])):
        print(guess_list[i][j])
