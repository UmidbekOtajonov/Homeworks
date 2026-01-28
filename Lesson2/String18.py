sentance = input("Enter a sentence: ")
items = sentance.split(" ")
if items[0] == items[-1]:
    print("words are equal")
else:
    print("words are not equal")