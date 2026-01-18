#dictionary simple principle {key:value}

spaces = "--------------------"
databank = {"feline": "cat",
            "poultry": "chicken",
            "vegetables": "broccoli",
            "fruit": "watermelon",}

data_items = databank.items()   #shows the whole key values within a dict
print(data_items)
print(spaces)

for data in databank:   #displays dict one by one
    print(data)
print(spaces)

data_keys = databank.keys() #display only keys
print(data_keys)
print(spaces)

data_values = databank.values() #display only values
print(data_values)
print(spaces)

databank.update({"feline":"lion"})  #rewriting/updating a certain key value within the dict
print(databank)
print(spaces)

databank.pop("poultry") #removes a certain key value within the dict
print(databank)
print(spaces)

databank.popitem()  #removes the last inserted key-value pair inside the dict
print(databank)
print(spaces)

databank.clear()    #empties the dict
print(databank)
print(spaces)

#adds them back
databank.update({"feline": "cat",
                "poultry": "chicken",
                "vegetables": "broccoli",
                "fruit": "watermelon",})
print(databank)