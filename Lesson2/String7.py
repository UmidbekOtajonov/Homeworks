sentance = input("Enter a sentence: ")
word = input("Enter a word: ")
last_char =sentance.split(" ")[-1]
print(last_char)
new_sent = sentance.replace(last_char, word)
print(new_sent)