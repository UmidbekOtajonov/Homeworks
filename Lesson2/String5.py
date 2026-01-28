words = input("enter a string :")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_count = 0
consonant_count = 0
for i in range(len(words)):
    if words[i] in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print("vowel_counts =" ,vowel_count, "consonant_counts =", consonant_count)