with open('data/words.txt', 'r') as file_read:
    for line in file_read:
        word = line[::-1]

        if line == word:
            print("this is palindrome..!")
        else:
            print("this is not palindrom..!")

