import json


with open("updates.json") as f:
    update_list = json.load(f)
    


updates_strings = []
for ver, updates in update_list.items():
    updates_strings.append(ver)
    updates_strings.extend(updates)
    
print("|".join(updates_strings) + "GEND")
