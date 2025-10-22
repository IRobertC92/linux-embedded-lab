#!/usr/bin/env python3
# =======================================================================================================================================================================
#  File        : morse_code_decode.py
#  Author      : Ionescu Robert-Constantin
#  Date        : 2025-10-21
#  Version     : 1.0
#  Description : Encode text into Morse code and decode Morse code back to text. Handles letters, digits, punctuation, and unknown characters gracefully.
# =======================================================================================================================================================================
#  Usage       : python3 morse_code_decode.py
# =======================================================================================================================================================================

# =======================================================================================================================================================================
# TO DO SECTION / Requirements
# ======================================================================================================================================================================= 
# TODO - STEP1   - Create a dictionary that maps each letter/digit to its Morse code equivalent.
# TODO - STEP2   - Create a function to convert the user input to morse code.
# TODO - STEP2.1 - Loop through each character in the text and look it up in the dictionary.
# TODO - STEP2.2 - Check if the character is matching and add it to the new list.
# TODO - STEP2.3 - Check for separate words, or space character and add the separator '\' in the list.
# TODO - STEP2.4 - Return the final result with the morse code characters.
# TODO - STEP3   - Invert the morse code dictionary to decoded morse code dictionary and use the initial keys and values viceversa.
# TODO - STEP4   - Create a function to decode the morse code and convert it to text.
# TODO - STEP4.1 - Create the first list which separates each morse code character and removes spaces.
# TODO - STEP4.2 - Create a second list with symbols used in morse code.
# TODO - STEP4.3 - Create a third list to check each symbol inside the decoded morse dictionary.
# TODO - STEP4.4 - Return the final list with the decoded characthers as text.

# =======================================================================================================================================================================
# Constants / Configuration / Data Structures
# =======================================================================================================================================================================

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-','V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--','Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--','4': '....-', '5': '.....',
    '6': '-....','7': '--...', '8': '---..',
    '9': '----.',
    '.': '.-.-.-',',': '--..--','?': '..--..','!': '-.-.--'
}
# Default separator for words
WORD_SEP = '/' 
# Inverted morse code dictionary
DECODE_MORSE = {morse: char for char, morse in MORSE_CODE.items()}

# =======================================================================================================================================================================
# Helper Functions
# =======================================================================================================================================================================

# Function to convert the user input to morse code
def encode_to_morse(user_input, WORD_SEP = "/"):
    user_input = user_input.upper()
    result = []
    # list comprehension usecase
    result = [MORSE_CODE.get(char, '?') if char != ' ' else WORD_SEP for char in user_input]
    return " ".join(result)

# Function to decode the morse code and convert it to text
def decode_from_morse(morse_text, WORD_SEP = "/"):
    morse_text = morse_text.strip().replace('/', WORD_SEP)
    word_chunks = morse_text.split(WORD_SEP)
    decoded_words = []

    # list comprehension usecase
    for word in word_chunks:
        word = word.strip()
        if not word:
            continue
        letters = [DECODE_MORSE.get(symbol, '?') for symbol in word.split()]
        decoded_words.append("".join(letters))
    return " ".join(decoded_words)

# =======================================================================================================================================================================
# Script Entry / Code Section
# =======================================================================================================================================================================

if __name__ == "__main__":
    print("Welcome to the Morse Code Converter!")
    print("Type 'exit' to quit the program.\n")
    
    while True:
        user_input = input("Enter text to convert to Morse:\n").strip()
        if user_input.lower() == 'exit':
            print("Exiting Morse converter. Goodbye!")
            break
        
        morse_text = encode_to_morse(user_input.upper(), WORD_SEP)
        print(f"\nConverted to Morse: {morse_text}")
        
        morse_decoded_text = decode_from_morse(morse_text, WORD_SEP)
        print(f"Decoded back: {morse_decoded_text.lower()}\n")
        print("-" * 40)