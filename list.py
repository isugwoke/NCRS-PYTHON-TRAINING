# [item1, item2, item3 .....]
my_list = [1,2,3,4,5,7,8, 100, 500]
my_list2 = ['ONE', 2, 3, 'Four', 'Michael', 200.12]

# List Indexing
# print(my_list[0])
# print(my_list2[4])

# Nested lists
nest_list = [1,2,3,[5,6,7,[8,9,10]]]
# print(nest_list[0])

# print(nest_list[3][3][0])



#  Lists are Mutable
# Sam to pam 

my_list = [1,2,3,4,5,7,8, 100, 500]

my_list[0] = 'One'
my_list[3] = 'Mike'

# print(my_list)

products = ['sugar', 'Garri', 'Milk', 'Fried Groundnut', 'water']
# print(products[0])

products[1] = 'shawarma'
# print(products)

# Length of a list
# print(len(products))

my_name = "James"
# print(len(my_name))
# print(len(nest_list))

# print(products[10]) #Error: Cant index non existing index


# List Methods
# 1. append - inserts an item at the end of a list
products = ['sugar', 'Garri', 'Milk', 'Fried Groundnut', 'water']

products.append("detergent")

# 2. insert - inserts item at a given index positioin
products.insert(2, 'Kulikuli')

# print(products)

# 3. pop - Removes an item from a list
products.pop()   #Removes the last item in the list

products.pop(3) #Removes an item at a given index position

# print(products)

# sort - Sorts a list in ascending order
my_list = ['a','f', 'd','e', 'b', 'c']
num_list = [100,500,300,200,600]
my_list.sort()
num_list.sort()

# print(my_list)
# print(num_list)

# reverse - Reverses the position of items in a list
num_list2 = [1,2,3,4,5]
num_list2.reverse()

# print(num_list2)

# List Slicing
products2 = ['sugar', 'Garri', 'Milk', 'Fried Groundnut', 'water']

print(products2[:3])
print(products2[1:])
print(products2[1:4])








