import json


def createBugList():
    # file_path = 'insect-orders.json'
    file_path = 'bug-list.json'

    try:
        with open(file_path, 'r') as fh:
            data = json.load(fh) # load json data from the file object and parses it into a python object 
        print("JSON data loaded from file")
        # print(f"Type of loaded data: {type(data)}") # <class 'dict'>
        # print(data)
        return data["orders"]
    except:
        print("error")

bugList = createBugList()

# print("bug in buglist")
# for bug in bugList["orders"]:
#     print(bug)
    

# print(bugList["orders"][0])


def searchBugList(order):
    for bug in bugList:
        if bug["order_name"] == order:
            print("match!")
            return bug["etymology"]
        else:
            print("searching...")

# Archaeognatha
# searchBugList("Archaeognatha")
print(searchBugList("Archaeognatha"))
# print(bugList["orders"])



