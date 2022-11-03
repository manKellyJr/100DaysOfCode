"""Bitmap Message by, Obed Banda
Displays a text message according to the provided bitmap image.

Tags: tiny, beginner, artistic"""

import sys

# There are 68 periods alng the top and bottom of this string:
# (You can als copy and paste this string from)


bitmap = """
....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
 ...................................................................."""

print("Bitmap message, by Obed Banda ")
print("Enter the message to display with the bitmap.")
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
             # Print an empty space since there's a space in the bitmap:
             print(' ', end='')
        else:
         # Print a character from the message:
         print(message[i % len(message)], end='')
    print()  # Print a newline.