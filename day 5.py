"""[P]     [L]         [T]            
[L]     [M] [G]     [G]     [S]    
[M]     [Q] [W]     [H] [R] [G]    
[N]     [F] [M]     [D] [V] [R] [N]
[W]     [G] [Q] [P] [J] [F] [M] [C]
[V] [H] [B] [F] [H] [M] [B] [H] [B]
[B] [Q] [D] [T] [T] [B] [N] [L] [D]
[H] [M] [N] [Z] [M] [C] [M] [P] [P]
 1   2   3   4   5   6   7   8   9 """

# amount from to

stacks = [
    [],
    ['H','B','V','W','N','M','L','P'],
    ['M','Q','H'],
    ['N','D','B','G','F','Q','M','L'],
    ['Z','T','F','Q','M','W','G'],
    ['M','T','H','P'],
    ['C','B','M','J','D','H','G','T'],
    ['M','N','B','F','V','R'],
    ['P','L','H','M','R','G','S'],
    ['P','D','B','C','N']
]

"""with open("5.txt", encoding="utf-8") as fail:
    for rida in fail:
        kasutu, amount, kasutu1, From, kasutu2 , to = rida.strip().split(" ")
        for i in range(0, int(amount)):
            stacks[int(to)].append(stacks[int(From)][-1])
            stacks[int(From)].pop(-1)
        #print(stacks[int(From)])
        #print(stacks[int(to)])

for stack in stacks:
    if stack != []:
        print(stack[-1], end='')"""

#print(stacks)

with open("5.txt", encoding="utf-8") as fail:
    for rida in fail:
        kasutu, amount, kasutu1, From, kasutu2 , to = rida.strip().split(" ")
        #print(stacks[int(From)])
        #print(stacks[int(to)])
        stacks[int(to)].extend(stacks[int(From)][-int(amount):])
        #print(amount)
        for i in range(int(amount)):
            #print(stacks[int(From)])
            stacks[int(From)].pop(-1)
        #print("")
        #print(stacks[int(From)])
        #print(stacks[int(to)])
        #print("")

for stack in stacks:
    if stack != []:
        print(stack[-1], end='')




