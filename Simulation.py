from random import randint

nb_sims = int(input("Choose the number of simulations "))
while nb_sims <= 0:
    nb_sims = int(input("Choose a positive number of simulations.. "))

nb_dice = int(input("Choose the number of dice "))
while nb_dice <= 0:
    nb_dice = int(input("Choose a positive number of dice.. "))

nbLT = 0
TTTDS = 0
for posbl_roll in range(1 * nb_dice, (6 * nb_dice) + 1):
    for sim in range(nb_sims):
        for NBD in range(1, nb_dice + 1):
            TTDS = randint(1, 6)
            TTTDS += TTDS
        nbL = 0
        while TTTDS != posbl_roll:
            TTTDS = 0
            for NBD in range(1, nb_dice + 1):
                TTDS = randint(1, 6)
                TTTDS += TTDS
            nbL += 1

        nbLT += nbL
        nbL = 0
    av_num_trws = nbLT / nb_sims
    nbLT = 0
    print("The average number of throws required to have", posbl_roll, "is",
          av_num_trws)
