"""
Using this file to create groups of developers if we would like to randomly
create groups of developers of equalish size.
"""
import random

DEV_LI = [
    "Noor",
    "Brady",
    "Dylan",
    "Sharala",
    "Lawrence",
    "Scott",
    "Aman",
    "Sarah",
    "Anthony",
    "Milos"
]

NUM_GROUPS = 2

def main():
    """a main method."""
    # get the total number of devs and the number of devs in each group
    num_devs = len(DEV_LI)
    # number of developers in each group
    group_size = num_devs // NUM_GROUPS
    # number we have to split the list at based on the
    # number of developers and group size
    partition = (num_devs + group_size - 1) // group_size

    # Shuffle the dev entries in DEV_LI
    random.shuffle(DEV_LI)

    # variable holding lists of developers
    # to get this we are partitioning the DEV_LI
    # for each partition add it to a list within rand_groups
    rand_groups = \
        [DEV_LI[i * group_size:(i + 1) * group_size] \
         for i in range(partition)]

    # check that the sum of all the groups is equal to the number of developers
    # essentially check if there is one group with one person in it for an odd split
    if group_size * NUM_GROUPS != num_devs:
        # select a random group (not the last one because it is the one with one dev)
        rand_group = random.randrange(0,NUM_GROUPS)
        # add the developer in the last group to the randon group
        rand_groups[rand_group].append(rand_groups[-1][0])
        # remove the small group from the list of groups
        rand_groups.pop(-1)

    count = 0
    # print each group
    for group in rand_groups:
        print("Group ", count + 1, ": ")
        print(group)
        count = count + 1

if __name__ == "__main__":
    main()
