#rivers

rivers = {
    'zambezi' : 'zambia',
    'orange' : 'south africa',
    'nile' : 'egypt',
    }
for river, country in rivers.items():
    print(river.title() + "'s favorite language is " + country.title() + ".")
