word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']

result = [ "*" if w in vowels else w for w in word ]

print("".join(result))


