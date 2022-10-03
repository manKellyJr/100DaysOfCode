#Testing aliens

alien_color = input("Enter the color of an alien 'green', 'yellow' or 'red': ")

alien_color = alien_color.lower()

if alien_color == 'green':
    print('\nYou have just earned 5 points\n')
elif alien_color == 'yellow':
    print('\nYou have earned 10 points\n')
    
elif alien_color == 'red':
    print('\nYou have earned 15 points\n')
else:
    print("\nNo such alien exist\n")
    
