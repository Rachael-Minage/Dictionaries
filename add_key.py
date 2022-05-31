# Write a Python script to add a key to a dictionary.
# sample_dictionary = {0:10,1:20}
# Using update()to add objects to a dictionary
from heapq import merge


dict_obj = {'a':'10', 'b':'20','c':'30'}
dict1 = {"d":"40","e":"50"}
dict_obj.update(dict1)
print(dict_obj)

sample_dictionary = {0:10,1:20}
sample_dictionary.update({2:30})
print(sample_dictionary)

sample_dictionary[5]=600
print(sample_dictionary)

# Write a Python script to concatenate following dictionaries to create a new one.
#  Use a for loop
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4 = {}
for d in (dict1,dict2,dict3):
    dict4.update(d)
print(dict4)

dict5= {7:79,9:54}
dict6 = (dict1|dict2|dict3|dict5)
print(dict6)

# Write a Python script to check whether a given key already exists in a dictionary

mydict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
}
def key_checker(key_value):
    if key_value in mydict.keys():
     print("Key exists")
    else:
     print ("Naah! check again")


key_checker("thirty")
