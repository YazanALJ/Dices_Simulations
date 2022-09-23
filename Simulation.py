from random import randint

nb_sims = int(input("Choose the number of simulations "))
while nb_sims <= 0:
    nb_sims = int(input("Choose a positive number of simulations.. "))

nb_dice = int(input("Choose the number of dice "))
while nb_dice <= 0:
    nb_dice = int(input("Choose a positive number of dice.. "))

nb_of_total_throws = 0
nb_of_throws = 0
dice_roll_sum = 0
for posbl_roll in range(1 * nb_dice, (6 * nb_dice) + 1):
    for sim in range(nb_sims):
        while dice_roll_sum != posbl_roll:
            dice_roll_sum = 0
            for NBD in range(1, nb_dice + 1):
                dice_roll_sum += randint(1, 6)
            nb_of_throws += 1
        nb_of_total_throws += nb_of_throws
        nb_of_throws = 0
        dice_roll_sum = 0
    av_num_trws = nb_of_total_throws / nb_sims
    nb_of_total_throws = 0
    print("The average number of throws required to have a score of", posbl_roll, "is",
          av_num_trws)
