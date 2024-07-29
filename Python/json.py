
#JSON function and dict
import json

x = {
    "name" : "Iz",
    "age" : 30,
    "married" : False,
    "pets" : ("Nigeru", "Christopher"),
    "children": None,
    "gadjets" : [
        {"model" : "Redmi Note 12+ Pro", "Price": 640},
        {"model" : "Ipad 9", "Price": 1409}
        ]
}

print(json.dumps(x, indent=2, separators = (":", "="), sort_keys=True))
