# You will write a program that implements a Caesar cipher, which is a simple method of encryption.
# A Caesar cipher takes the letters of a message and shifts each letter along the alphabet by a certain number of places.


# Define a function called getDoubleAlphabet that takes a string argument and concatenates, or combines, the given string with itself as follows

def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Functions should perform a specific task.
# Usually, because functions perform a specific task, your functions will also probably be short.
# Though this function returns a string, it doesn’t take an argument like the getDoubleAlphabet() function.

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# The cipher key is how far you will shift the letters. By using two alphabets, you can have a cipher key that is any integer from 1 to 25.
# Don’t count the key at index 26 because that key would shift you back to the original message.

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Take three arguments: the message, the cipherKey, and the alphabet.
# Initialize variables.
# Use a for loop to traverse each letter in the message.
# For a specific letter, find the position.
# For a specific letter, determine the new position given the cipher key.
# If current letter is in the alphabet, append the new letter to the encrypted message.
# If current letter is not in the alphabet, append the current letter.
# Return the encrypted message after exhausting all the letters in the message.

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Functions are useful because you can reuse them. You will write a decryptMessage() function by reusing the encryptMessage() function.
# For this simple encryption, you can undo the encryption by shifting each letter back. Thus, instead of adding the cipher key, you will subtract the cipher key.
# To avoid rewriting most of the logic, you will pass in a negative cipher key.

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# You have built a collection of user-defined functions that will help you write a Caesar cipher program. The main logic of the program will, of course, also be contained in a function.

# Define a string variable to contain the English alphabet.
# To be able to shift letters, double your alphabet string.
# Get a message to encrypt from the user.
# Get a cipher key from the user.
# Encrypt the message.
# Decrypt the message.

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

# Call the function

runCaesarCipherProgram()