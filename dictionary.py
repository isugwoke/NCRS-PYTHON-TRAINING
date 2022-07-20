# Key value pairs
# Unordered 
# list = [1,2,'four']
# {key1: value1, key2: value2 ...}

from pydoc import Helper


bio_data = {'name':'Mike', 'age':45, 'job':"programmer"}
print(bio_data['name'])
print(bio_data['job'])
print(bio_data['age'])

# Nested dictionaries
mike_data = {'name':'Mike', 'age':15, 'job':"programmer", 'mother':{'name': 'Tabitha', 'age': 50, 'addr': 'Bukuru Jos'}}

print(mike_data['job'])
print(mike_data['mother']['name'])
print(mike_data['mother']['addr'])

helen_data = {'name':'Helen', 'age':45, 'job':"programmer"}
helen_data['numb_children'] = 4

print(helen_data)

# dictionaries are mutable

# Read up on these 2 data structures
# 1. Tuples
# 2. sets

