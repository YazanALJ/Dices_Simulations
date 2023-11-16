from random import randint
from math import floor, comb


def fetch_user_input() -> tuple[int, int, int]:
    """
    Prompts the user for input for the number of simulations, number of dice, and number of dice faces.

    Returns:
        A tuple containing the number of simulations, number of dice, and number of dice faces as integers.
    """
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


def compute_actual_probability(tot_sum: int, nb_dice: int, faces: int) -> float:
    """
    Computes the actual probability of rolling a given total sum with a given number of dice, each with a given
    number of faces.

    Args:
        tot_sum: The total sum to be rolled.
        nb_dice: The number of dice being rolled.
        faces: The number of faces on each die.

    Returns:
        The actual probability of rolling the given total sum with the given number of dice and die faces.
    """
    res = 0
    for k in range(floor(((tot_sum - nb_dice) / faces) + 1)):
        res += (-1) ** k * comb(nb_dice, k) * comb((tot_sum - faces * k - 1), nb_dice - 1)
    return res * (1 / faces ** nb_dice)


def throw_n_dice(nb_dice: int, die_faces: int) -> int:
    """
    Throws a given number of dice with a given number of faces.

    Args:
        nb_dice: The number of dice to throw.
        die_faces: The number of faces on each die.

    Returns:
        The sum of the values rolled on the dice.
    """
    dice_roll_sum = 0
    for NBD in range(1, nb_dice + 1):
        dice_roll_sum += randint(1, die_faces)
    return dice_roll_sum


def throws_until_obtainment(nb_dice: int, desired_roll: int, die_faces: int) -> int:
    """
    Keeps throwing dice until a desired roll is obtained, and returns the number of throws required to obtain it.

    Args:
        nb_dice: The number of dice to throw.
        desired_roll: The desired roll to obtain.
        die_faces: The number of faces on each die.

    Returns:
        int: The number of throws required to obtain the desired roll.
    """
    nb_of_throws = 0
    while True:
        nb_of_throws += 1
        if throw_n_dice(nb_dice, die_faces) == desired_roll:
            break
    return nb_of_throws


def dice_master(nb_sims: int, nb_dice: int, die_faces: int) -> None:
    """
    Simulates rolling dice and calculates the average number of throws required to obtain each possible roll, as well as
    the actual probability of obtaining each roll.

    Args:
        nb_sims: The number of simulations to run.
        nb_dice: The number of dice to throw.
        die_faces: The number of faces on each die.
    """
    for posbl_roll in range(1 * nb_dice, (die_faces * nb_dice) + 1):
        nb_of_total_throws = 0
        for sim in range(nb_sims):
            nb_of_total_throws += throws_until_obtainment(nb_dice, posbl_roll, die_faces)
        av_num_trws = nb_of_total_throws / nb_sims
        print(f"The average number of throws required to have a score of {posbl_roll: <2} is "
              f"{av_num_trws: <10.1f} which corresponds to {(1 / av_num_trws): <9.4%} in contrast the the actual "
              f"probability of {compute_actual_probability(posbl_roll, nb_dice, die_faces):.4%}")


def start():
    """
    Entry point for the program. Prompts the user for input and runs the dice simulation.
    """
    nb_sim, nb_dice, die_faces = fetch_user_input()
    dice_master(nb_sim, nb_dice, die_faces)


start()
