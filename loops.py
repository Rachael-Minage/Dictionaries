a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)

for key in a_dict:
    print(key,a_dict[key])

# Iterating through using .items()
the_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
dict_items = the_dict.items()
print(dict_items)

# for value in a_dict:
#     print(value)

for item in dict_items:
    print(item)

knights = {"gallahad":"the pure","robin":"the brave"}
for k,v in knights.items():
    print(k,v)

# Enumerate().. returns index pst and corresponding value at the same time
for i,v in enumerate(knights):
    print(i,v)
#zip() loops over two or more sequences at the same time

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print("what is your {0}, it's {1}".format(q,a))

for value in a_dict.values():
    print(value)

# prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for key in prices.keys():
#     if key == 'orange':
#         del prices[key]

    

