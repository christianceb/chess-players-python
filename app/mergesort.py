def merge_sort(list):
    """Merge sort, duh?

    :param list: List of things to sort
    :return: Cool sorted list
    """
    if len(list) > 1:
        middle = len(list) // 2
        left = merge_sort(list[:middle])  # Sort left partition
        right = merge_sort(list[middle:])  # Sort right partition

        list = []

        # As long as we have stuff to sort, we run this routine
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                list.append(left[0])
                left.pop(0)
            else:
                list.append(right[0])
                right.pop(0)

        # Merge left partition items to list
        for item in left:
            list.append(item)

        # and then the right
        for item in right:
            list.append(item)

    return list