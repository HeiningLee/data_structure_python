def strip_sentence():
    my_sentence = input("Please input your sentence: ")
    list_sym1 = [i for i in range(33, 48)]
    list_sym2 = [i for i in range(58, 65)]
    list_sym = list_sym1 + list_sym2
    # print(list_sym)
    striped_sentence = ''
    for c in my_sentence:
        if ord(c) not in list_sym:
            striped_sentence += c

    print("striped as: " + striped_sentence)


strip_sentence()
