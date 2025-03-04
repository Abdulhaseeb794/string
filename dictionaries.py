my_dict = {'brand': 'ford', 'model': 'mustang'}
print(my_dict)

# update value
my_dict['model'] = 'f150'
print(my_dict)

# add ne key_value pair
my_dict['year'] = 2020
print(my_dict)

# remove key_value pair
my_dict.pop('year')
print(my_dict)

# Deleting a key-value pair in Dictionary using del() Method :
del my_dict['model']
print(my_dict)

# clear dictionary
my_dict.clear()
print(my_dict)

