# By Veronica Salm

# Useful skills for students to know:
# - how to seed the random function
# - how to map one range (0 to 1.0 from random.random) to a smaller, weighted range

# Using the example: flip an unfair coin

import random

# a global seed constant for the random function
my_seed = 2**32-1


def unfair_coin_flip(prob_heads, prob_tails):
    """ Takes two floating point values, the probabilities of 
    heads and tails respectively, and returns a single weighted 
    coin flip.

    This is similar to what students will need to do in the
    assignment, but they need to instead generate n rolls for 
    an n-sided object. This is a good first step.

    Note that it is guaranteed that prob_heads + prob_tails = 1

    Arguments:
        prob_heads (float): the probability of heads from 0 to 1
        prob_tails (float): the probability of tails from 0 to 1

    Returns:
        "HEADS" or "TAILS" based on the result of the coin flip

    """
    # map prob_heads and prob_tails

    # you can do this a different way if desired
    # but using a 2-element list will simulate what students
    # will need to do in the assignment 
    # right now this is only 2-dimensional, but they will 
    # implement an n-dimensional version
    mapping = [None, None] 

    # map the values
    # set the upper bound of each type 
    mapping[0] = 0 + prob_heads

    # set probability of tails (this should always equal 1)
    mapping[1] = mapping[0] + prob_tails

    # now we flip the coin
    flip = random.random()

    # print("Random number: ", flip)

    if flip < mapping[0]:
        return "HEADS"

    else:
        return "TAILS"



if __name__ == "__main__":

    # begin by seeding the random module
    random.seed(my_seed)

    for i in range(10):
        print(unfair_coin_flip(0.75, 0.25))

    print("\n")

    # show that if we re-seed the random module
    # we get the same result
    random.seed(my_seed)

    for i in range(10):
        print(unfair_coin_flip(0.75, 0.25))
