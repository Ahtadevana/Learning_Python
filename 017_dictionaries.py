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

databank.update({"feline":"lion"})  #rewriting/updating a certain key value within a dict
print(databank)
print(spaces)

databank.pop("poultry") #removes a certain key value within a dict
print(databank)
print(spaces)

databank.popitem()  #removes the latest key value added into the dict
print(databank)
print(spaces)

databank.clear()    #entirely remove a dict to an empty one
print(databank)
print(spaces)

#adds them back
databank.update({"feline": "cat",
                "poultry": "chicken",
                "vegetables": "broccoli",
                "fruit": "watermelon",})
print(databank)