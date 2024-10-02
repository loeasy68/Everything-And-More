dictionary = {"Bub Bub": 0, "Hiiiii": "lol"}
value = list(dictionary.keys()) # dictionary.keys() returns key values and list makes it a list.
print(value[0]) # This is the index of the key we are printing
#Debugging Purposes, The value variable is just the dictionary's keys in a list, NOTE: That the values will get concataned as showned in the example below. NOTE: value will not contain the values. It will only contains the keys.
print(dictionary[value[1]]) # How to get the value