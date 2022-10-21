from random import randint

# Idea 1: print a theoritical probability of a given score, this will require using a formula using the binomial distribution


def fetch_user_input():
    nb_sims = int(input("Choose the number of simulations "))
    while nb_sims <= 0:
        nb_sims = int(input("Choose a positive number of simulations... "))

    nb_dice = int(input("Choose the number of dice "))
    while nb_dice <= 0:
        nb_dice = int(input("Choose a positive number of dice... "))

    dice_faces = int(input("Choose the number of die faces "))
    while dice_faces <= 0:
        dice_faces = int(input("Choose a positive number of dice faces... "))
    return nb_sims, nb_dice, dice_faces


def throw_n_dice(nb_dice, die_faces):
    dice_roll_sum = 0
    for NBD in range(1, nb_dice + 1):
        dice_roll_sum += randint(1, die_faces)
    return dice_roll_sum


def throws_until_obtainement(nb_dice, desired_roll, die_faces):
    nb_of_throws = 0
    while True:
        nb_of_throws += 1
        if throw_n_dice(nb_dice, die_faces) == desired_roll:
            break
    return nb_of_throws


def dice_master(nb_sims, nb_dice, die_faces):
    for posbl_roll in range(1 * nb_dice, (die_faces * nb_dice) + 1):
        nb_of_total_throws = 0
        for sim in range(nb_sims):
            nb_of_total_throws += throws_until_obtainement(nb_dice, posbl_roll, die_faces)
        av_num_trws = nb_of_total_throws / nb_sims
        print(f"The average number of throws required to have a score of {posbl_roll} is "
              f"{av_num_trws:.1f} which corresponds to {(1 / av_num_trws):.10%}")


def start():
    nb_sim, nb_dice, die_faces = fetch_user_input()
    dice_master(nb_sim, nb_dice, die_faces)


start()
