"""Diamons by, Obed Banda
Draws diamonds of various sizes.

                             /\       /\
                            /  \     //\\
              /\     /\    /    \   ///\\\
             /  \   //\\  /      \ ////\\\\
   /\   /\  /    \ ///\\\ \      / \\\\////
  /  \ //\\ \    / \\\///  \    /   \\\///
  \  / \\//  \  /   \\//    \  /     \\//
   \/   \/    \/     \/      \/       \/
Tags: tiny, beginner, artistic"""


def main():
    print ('Diamons, by Obed Banda')
    # Display diamonds of sizes 0 through 6:
    for diamondSize in range(0, 6):
        displayOutlineDiamond(diamondSize)
        print()  # Display a new line.
        displayFilledDiamond(diamondSize)
        print()


def displayOutlineDiamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i -1), end='')  # left side space.
        print('/', end='')  # Left side of diamond.
        print(' ' * (i * 2), end='') # Interior of diamond
        print('\\')  # Right side of diamond.

    # Display the bottom half of the diamond:
    for i in range(size):
        print(' ' * (size - i -1), end='')  # left side space.
        print('\\', end='')  # Left side of diamond.
        print(' ' * (i * 2), end='') # Interior of diamond
        print('/')  # Right side of diamond.


def displayFilledDiamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # left side space.
        print('/', end='')  # Left side of diamond.
        print('\\')  # Right side of diamond.

    # display the top of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # left side space.
        print('\\', end='')  # Left side of diamond.
        print('/')  # Right side of diamond.


if __name__ == '__main__':
    main()
