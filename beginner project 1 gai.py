import random
h = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
    "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="
]
w_list = ["python", "hangman", "challenge", "programming", "random"]
w = list(random.choice(w_list))
w_set = set(w)
t_set = set()
i = 0
c = []

for l in w:
    if l in w_set:
        c.append("_")
    else:
        c.append(l)
a = False
print("Welcome to Hangman")
print("You have 7 lives")
while not a:
    print(h[i])
    print("Current state: " + " ".join(c))
    print("You have tried: ", " ".join(t_set))
    g = input("Guess a letter: ").lower()
    if g in t_set:
        print("You've already tried that letter.")
        continue
    t_set.add(g)
    if g in w_set:
        for j, l in enumerate(w):
            if l == g:
                c[j] = l
    else:
        i += 1
    if "_" not in c:
        print("Congratulations! You won!")
        a = True
    elif i == 6:
        print(h[i])
        print("You lose! The word was: " + "".join(w))
        a = True
