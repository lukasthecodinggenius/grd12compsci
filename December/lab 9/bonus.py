sentence = input("Enter a sentence: ")
words = sentence.split() #split sentance into its words
frequencies = {}

for word in words:
    if word in frequencies:
        frequencies[word] += 1 #add word to dict for each word in sentance
    else:
        frequencies[word] = 1

print("Word frequencies:")
for word, count in frequencies.items():
    print(word + ":", count) #go thru dictionary and print the word and how many times it shows up in the sentance
