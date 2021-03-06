# skill algorithm
from .common import remove_duplicates


def remove_covers(input_list):
    """
    Removes sets that are covered by another set in a list
    :param input_list: list
    :return: list
    """

    output_list = []
    for subset in input_list:
        il_temp = input_list.copy()
        il_temp.remove(subset)
        intersects = False
        covered = False
        for subset_temp in il_temp:
            if len(subset.intersection(subset_temp)) > 0:
                intersects = True
                if len(subset) <= len(subset_temp) and subset.intersection(subset_temp) == subset:
                    covered = True
        if not intersects:
            output_list.append(subset)
        elif not covered:
            output_list.append(subset)

    return output_list


def skill(pc, states_list):
    """
    Producs a list of MCCs from a pairchart and its states
    :param pc: pairchart dictionary
    :param states_list: list
    :return: list of MCC lists
    """

    print('\nDetermining maximum compatibility classes...')

    sl_rev = states_list.copy()
    sl_rev.reverse()
    num_states = len(states_list)

    big_l = []  # start with empty list

    current_state_num = num_states
    for k in sl_rev:
        compared_states = states_list[current_state_num:]

        sk = set()
        for state in compared_states:
            if pc[k][state].compatible:
                sk.add(state)

        l_prime = []
        for subset in big_l:
            lp_subset = sk.intersection(subset)
            lp_subset.add(k)
            l_prime.append(lp_subset)
        l_prime.append(set(k))
        l_prime = remove_duplicates(l_prime)

        for lp_subset in l_prime:
            big_l.append(lp_subset)
        big_l = remove_covers(big_l)

        current_state_num -= 1

    mccs = []
    for subset in big_l:
        mccs.append(sorted(subset))
    mccs = sorted(mccs)
    mccs.reverse()
    mccs.sort(key=len)
    mccs.reverse()
    print(mccs)
    return mccs
