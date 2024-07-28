
# Count vowels and consonants in a String

def count_vowels_and_consonants(s):

    # Define sets of vowels and consonants
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    # Initialize counters
    vowel_count = 0
    consonant_count = 0

    # Iterate through each character in the string
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count


# Test the function
vowels, consonants = count_vowels_and_consonants("my name is varun")
print(f"Vowels: {vowels}, Consonants: {consonants}")  # Output: Vowels: 5, Consonants: 8
