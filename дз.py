def isPalindrom(word):
    word2 = word[: int(len(word) / 2)]
    word3 = word[int(len(word) / 2) : int(len(word) / 2) * 2]
    print(word2 == word3[::-1])

word = input('введите слово-палиндром: ')
isPalindrom(word)