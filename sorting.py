# Using operator.itemgetter() to sort a dictionary
from audioop import reverse
import operator
sample_dict ={"Product":"iPhone 13 Pro Max","Company": "Apple"}
print(operator.itemgetter("Product")(sample_dict))
print(operator.itemgetter("Company")(sample_dict))

# Sorting by name(Alphabetical order)
phones = [{'phone_name':'Apple','phone_price': 113000},
          {'phone_name':'Samsung','phone_price':109999},
          {'phone_name':'OnePlus','phone_price':69000}
]
# To sort by company names pass phone_name in itemgetter()
sorted_dict_key = sorted(phones, key = operator.itemgetter("phone_name"))
print(sorted_dict_key)

sorted_dict_descend = sorted(phones,key =operator.itemgetter("phone_name"),reverse=True)
print(sorted_dict_descend )

sorted_prices = sorted(phones,key = operator.itemgetter('phone_price'))
print(sorted_prices)
sorted_price_descending = sorted(phones,key = operator.itemgetter('phone_price'),reverse=True)
print(sorted_price_descending)
# sorting by value
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = sorted(d.items(), key =operator.itemgetter(1))
print(sorted_d)

d_2={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d2 = sorted(d.items(), key =operator.itemgetter(0))
print(sorted_d2)

colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
sorted_colors = sorted(colors.items(), key=operator.itemgetter(0))
print(sorted_colors)

colors_2 = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
sorted_colors2 = sorted(colors.items(), key=operator.itemgetter(1))
print(sorted_colors2)


def sort_values(dict):
    sorted_dict = sorted(dict.items(),key= operator.itemgetter(1))
    return sorted_dict

print(sort_values({"fanta":500, "coke":50, "ribena":100,"sprite":1000}))

def sort_keys(dict):
    sorted_dict = sorted(dict.items(),key= operator.itemgetter(0))
    return sorted_dict

print(sort_keys({"fanta":500, "coke":50, "ribena":100,"sprite":1000}))

