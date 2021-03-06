def find_stable_marriages(bachelors, bachelorettes):
    """

    Implementation of Gale-Shapley algorithm for solving the Stable Marriage Problem
    :param bachelors: dictionary where keys are the bachelors and
        the values are a list of bachelorettes in order of preferences
    :param bachelorettes: dictionary where keys are the bachelorettes
        and the values are a list of bachelors in order of preferences
    :return: dictionary of stable marriages where keys are the husband and values are the wife

    """
    
    marriages = {}
    current_bachelors = [b for b in bachelors.keys() if b not in marriages]

    # keep running till all bachelors are assigned a partner
    while current_bachelors:
        # select first bachelor remove from list
        bachelor = current_bachelors.pop(0)
        # select first choice and remove from list:
        #   this keeps track of partners the bachelor has already tried
        first_choice = bachelors[bachelor].pop(0)

        if first_choice not in marriages.values():
            marriages[bachelor] = first_choice
        else:
            rank_of_bachelor = bachelorettes[first_choice].index(bachelor)
            # invert dictionary to make it easy to get the current_partner of bachelorette
            marriages_by_bachelorette = {val: key for key, val in marriages.items()}
            current_partner = marriages_by_bachelorette[first_choice]
            rank_of_current_partner = bachelorettes[first_choice].index(current_partner)

            # switch partners if first_choice prefers bachelor over current_partner
            if rank_of_bachelor < rank_of_current_partner:
                marriages[bachelor] = first_choice
                # move current_partner back to bachelors list
                del marriages[current_partner]
                current_bachelors.append(current_partner)
            else:
                # add bachelor back to current_bachelors list
                current_bachelors.append(bachelor)

    return marriages


def main():
    
    bachelors = {"a": [5, 3, 2, 4, 1],
                 "b": [1, 3, 4, 5, 2],
                 "c": [5, 3, 2, 1, 4],
                 "d": [1, 3, 2, 5, 4],
                 "e": [2, 4, 1, 5, 3]}

    bachelorettes = {1: ["a", "c", "d", "e", "b"],
                     2: ["a", "c", "e", "b", "d"],
                     3: ["a", "e", "d", "c", "b"],
                     4: ["a", "e", "b", "c", "d"],
                     5: ["a", "d", "c", "b", "e"]}

    print(find_stable_marriages(bachelors, bachelorettes))


if __name__ == '__main__':
    main()
