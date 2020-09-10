def player_search_g(list, value):
    """DEPRECATED: Player Search - (G)reedy

    (Deprecated as assessment tool was inconsistent.)

    Search all items in the list but do not stop even if it has been found

    :param list:
    :param value:
    :return:
    """
    found = []
    middle = len(list) // 2

    # Check if middle is what we're looking for
    if list[middle].contains(value):
        found.append(list[middle])

    if len(list) > 1:

        left_found = player_search_g(list[:middle], value)
        right_found = player_search_g(list[middle:], value)

        found = left_found + found + right_found

    return found


def player_bs_l(list, value, step=0, silent=False):
    """Player (B)inary (S)earch (L)ast name

    Search, stop and return object once it matches parameters

    :param list: Set to look for
    :param value: Value to match
    :param step: Number of steps the search have already taken
    :param silent: Keep this function from printing the steps
    :return: None if not found, the matching object otherwise
    """

    found = None
    step += 1
    if not silent:
        print("Step count: " + str(step))

    if len(list) > 1:
        middle = len(list) // 2

        if list[middle].last == value:
            found = list[middle]
        else:
            if list[middle].last < value:
                found = player_bs_l(list[middle:], value, step, silent)
            else:
                found = player_bs_l(list[:middle], value, step, silent)

    return found
