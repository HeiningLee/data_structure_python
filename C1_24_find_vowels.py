def find_vowels():
    astring = input("Please input a string: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    for char in astring:
        if char in vowels:
            num_vowels += 1
    print("There are " + str(num_vowels) + " vowels in your string.")

find_vowels()
