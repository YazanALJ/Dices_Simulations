from random import randint


def fetch_user_input():
    nb_sims = int(input("Choose the number of simulations "))
    while nb_sims <= 0:
        nb_sims = int(input("Choose a positive number of simulations.. "))

    nb_dice = int(input("Choose the number of dice "))
    while nb_dice <= 0:
        nb_dice = int(input("Choose a positive number of dice.. "))
    return nb_sims, nb_dice


def throw_n_dice(nb_dice):
    dice_roll_sum = 0
    for NBD in range(1, nb_dice + 1):
        dice_roll_sum += randint(1, 6)
    return dice_roll_sum


def throws_until_obtainement(nb_dice, desired_roll):
    nb_of_throws = 0
    while True:
        nb_of_throws += 1
        if throw_n_dice(nb_dice) == desired_roll:
            break
    return nb_of_throws


def dice_master(nb_sims, nb_dice):
    for posbl_roll in range(1 * nb_dice, (6 * nb_dice) + 1):
        nb_of_total_throws = 0
        for sim in range(nb_sims):
            nb_of_total_throws += throws_until_obtainement(nb_dice, posbl_roll)
        av_num_trws = nb_of_total_throws / nb_sims
        print(f"The average number of throws required to have a score of {posbl_roll} is "
              f"{av_num_trws:.1f} which corresponds to {(1 / av_num_trws):.10%}")


def start():
    nb_sim, nb_dice = fetch_user_input()
    dice_master(nb_sim, nb_dice)


start()
