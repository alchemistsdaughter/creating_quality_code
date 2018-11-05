"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurants_small.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)
    

    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines_list = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """
    name_to_cuisines = invert(cuisine_to_names)
    
    cuisines = set(cuisines_list)
    
    filtered_names = [name for name in names_matching_price if len(cuisines.intersection(set(name_to_cuisines[name]))) > 0]
    
    
# =============================================================================
#     for name in names_matching_price:
#         cur_cuisines = set(name_to_cuisines[name])
#         if len(cur_cuisines.intersection(cuisines)) > 0:
#             filtered_names.append(name)
# =============================================================================
# =============================================================================
#         for c in name_to_cuisines[name]:
#             if c in cuisines_list:
#                 filtered_names.append(name)
#                 break
# =============================================================================
    
    return filtered_names

def invert(cuisine_to_names):
    result = {}
    
    for k in cuisine_to_names:
        for val in cuisine_to_names[k]:
            if val in result:
                result[val].append(k)
            else:
                result[val] = [k]
    
    return result

names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
cuis = {'Canadian': ['Georgie Porgie'],
'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
'Malaysian': ['Queen St. Cafe'],
'Thai': ['Queen St. Cafe'],
'Chinese': ['Dumplings R Us'],
'Mexican': ['Mexican Grill']}
cuisines_list = ['Chinese', 'Thai']
print(filter_by_cuisine(names, cuis, cuisines_list))

def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    """

    name_to_rating = {} #creates the dictionary - currently empty
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}
    
    with open(file) as f:
        name = None
        c = 0
        for line in f:
            if c == 0:
                name = line.strip()
            elif c == 1:
                rating = line.strip()
                name_to_rating[name] = rating #adding value to the dictionary
            elif c == 2:
                price = line.strip()
                price_to_names[price].append(name)
            elif c == 3:
                cuisines = line.strip().split(',')
                for cui in cuisines:
                    if cui in cuisine_to_names:
                        cuisine_to_names[cui].append(name)
                    else:
                        cuisine_to_names[cui] = [name]
            if c == 4:
                c = 0
            else:
                c += 1
    return name_to_rating, price_to_names, cuisine_to_names 
                    
                
recommend(FILENAME, '$', 'Chinese')
