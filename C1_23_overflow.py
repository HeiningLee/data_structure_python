mylist = [0, 1, 2, 3, 4, 5]
i = 0
while True:
    try:
        print(mylist[i])
        i += 1
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
        break
