import json

from .homely import model
 
# Opening JSON file
with open('./test/respone-examples/locations.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
 
    for l in data:
        print(l)
        loc1 = model.Location(l)
        print(loc1.name)
 
    # Print the data of dictionary
  