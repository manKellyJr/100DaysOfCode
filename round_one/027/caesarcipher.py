"""Caesar Cipher, by Obed Banda
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.


Tags: short, beginner, cryptography, math"""

try:
    import pyperclip    # pyperclip copies text to the clipboard.
except ImportError:
    pass    # If pyperclip is not installed, do nothing. Its no big deal.

# Every possible symbol that  can be encrypted/decrypted:
# (!) You can add numbers and punctuationmarks to encrypt those
# symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar cipher by, Obed')
print("The Caesar cipher encrypt letters by shiffting them over by a")
print('key number. For example, a key of 2 means that letter A is')
print('encrypted to C, the letter B encrypted int D, and so on')
print()

# Let the user enter if they are encrypting or decrypting:
while True:  # Keep asking until the user enters  e or d.
    print('Do you want to (e)ncrypt or (d)ecrypt')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the e or d')

while True:  # Keep asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break





