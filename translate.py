# Homework 4, translate.py
#
# Eric Kye
#
# To take a word from the user and check the first index of the word.
# We want to translate the word into pig latin.

# Prompt user to input a word.
word=input("Enter a word to translate:")

# Convert all of the letters in the word to lower case.
word =word.lower()

# We loop through each letter in the word
for letters in word:

    # We check if the first letter is a vowel.
    if letters[0] in 'aeiou':
        # if the first letter is a vowel, we just simply add 'way' to the end of the word. We can just concatenate the strings
        word=word+"way"
        # we break out of the loop is this condition is met. 
        break
    else:
        # If it is a consonant, we take the letters after the first letter until the end of the word. Then we take the first letter and add it to the end of that substring. We then add 'ay' after. 
        word = word[1:] + word[0] +"ay"
        break

print("Pig latin:", word)

    
