word = input()
vowels = 0
for vowels_in in word:
        if vowels_in.isalpha():
            if vowels_in.lower() in 'aeiouyауоыиэяюёе':
                vowels += 1
print(vowels)

