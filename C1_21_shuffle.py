import random


def my_shuffle(iter):
    len_iter = len(iter)
    for index in range(len_iter):
        index_rand = random.randint(0, len_iter-1)
        iter[index], iter[index_rand] = iter[index_rand], iter[index]
    return iter


s = [0, 1, 2, 3, 4, 5]
print(my_shuffle(s))

