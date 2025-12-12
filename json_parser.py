import json  
def tema(name):
    with open('data.json', 'r', encoding="utf-8") as file:  
        data = json.load(file)
    if name.lower() == "наука":
        return data["topics"][0]['questions']
    if name.lower() == "кино":
        return data["topics"][1]['questions']
    if name.lower() == "история":
        return data["topics"][2]['questions']
# print(tema('кино'))
