with open('data/words.txt', 'r') as file:
    for line in file:
        line = line.strip()

        def palindrome(s):
            return s == s[::-1]

        ans = palindrome(line.strip())

        if ans:
            print("this is palindrome..!")
        else:
            print("this is not palindrom..!")