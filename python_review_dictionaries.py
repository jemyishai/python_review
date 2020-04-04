"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}

def cities_to_add (city,country,continent):
    continent_key = locations.get(continent, 'NOPE')
    if continent_key != 'NOPE':
      country_key = continent_key.get(country,"NOPE")
      if country_key != "NOPE":
          #this check is needed in the event there is more than one city in the country
          if city not in country_key:
              country_key.append(city)
              country_key.sort()
          else:
              print 'city already added'
      else:
          continent_key[country] = [city]
    else:
        locations[continent] = {country: [city]}

cities_to_add("Shanghai","China","Asia")
cities_to_add("Bangalore","India","Asia")
cities_to_add("Atlanta","USA","North America")
cities_to_add("Cairo","Egypt","Africa")

# print(locations)

def print_array(input):
    for item in input:
        print item

def asia_alpha_order(location):
    asiancities = []
    citiescountry = []
    asian_co = location['Asia']
    for key in asian_co:
        asiancities = asiancities + asian_co[key]
        asiancities.sort()
    for city in asiancities:
        for country in asian_co.keys():
            if city in asian_co[country]:
                citiescountry.append(city + ' - ' + country)
    return citiescountry

print('1')
print_array(locations['North America']['USA'])
print('2')
print_array(asia_alpha_order(locations))

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
