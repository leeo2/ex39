# Olivia Lee
# 11-6-19
# Dictionaries

# Create a mapping of state to abbreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", [states['Michigan']])
print("Florida's abbreviation is: ", [states['Florida']])

# do it by using the state that cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abrev in list(states.items()):
    print(f"{state} is abbreviated {abrev}")

# Print every city in state
print('-' * 10)
for abrev, city in list(cities.items()):
    print(f"{abrev} has the city {city}")


# Now do both at the same time
print('-' * 10)
for state, abrev in list(states.items()):
    print(f"{state} state is abbreviated {abrev}")
    print(f"and has city{cities[abrev]}")


print('-' * 10)
# Safely get an abbreviation by state that might not be there
state = states.get('Texas')

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
