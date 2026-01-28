text = input("Enter text: ")
words = text.split()
first_letters = [w[0] for w in words]
new_word = "".join(first_letters)
print(new_word)


