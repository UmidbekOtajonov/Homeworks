word_1 = input("Enter a word: ")
word_2 = input("Enter a word: ")
if word_1 in word_2:
    print(f" {word_1} in  {word_2}")
elif word_2 in word_1:
    print(f" {word_2} in  {word_1}")
else:
    print("word not contains another words")
