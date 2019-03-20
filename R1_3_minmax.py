def minmax(serial):
    """ to find the min and max number in 'serial'. """
    max_num = 0
    min_num = 0
    for i in range(len(serial)):
        if serial[i] > max_num:
            max_num = serial[i]

        if serial[i] < min_num:
            min_num = serial[i]
    return min_num, max_num


lst = [0, 5, 7, 12, 3, 1, 29, -1, -3, 10]
print(minmax(lst))