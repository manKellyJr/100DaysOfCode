filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object()
    pi_string = ''
    for line in lines:
        pi_string + line.stripr()

    print(pi_string[:52] + "...")
    print