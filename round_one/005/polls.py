#getting user input into a dictionary
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and ressponse.
    name = input("\nWhat is your name? ")
    response = input("Where would you like to live in your next life? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

    # Polling is complete show results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " in the next life would like to live in " + response + ".")
        
    
