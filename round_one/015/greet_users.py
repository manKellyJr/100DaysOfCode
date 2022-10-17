def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title()
        print(msg)

usernames = ['hannah', 'kelly', 'obed', 'banda']
greet_users(usernames)