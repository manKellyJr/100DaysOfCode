def show_magicians(magicians):
    """A function tha print a list of names of magicians"""
    for name in magicians:
        print(name.title())


list_of_magicians = ['obed', 'kelly', 'jr', 'banda']

def make_great(magicians):
    for name in magicians:
        name = name.title() + ' the Great'
        print(name)


make_great(list_of_magicians)
show_magicians(list_of_magicians)

