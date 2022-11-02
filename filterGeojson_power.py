import json

f = open("power_alpsmin.geojson",encoding="utf8")
print(f)
file = json.load(f)
ignoredItems = 0
newfile = {}
newfile["type"] = "FeatureCollection"
newfile["name"] = file["name"] + "f"
newfile["crs"] = file["crs"]
newfile["features"] = []

filterterms= ["line","minor_line"]
 

for i in range (len(file["features"])):

    
   
    if file["features"][i]["properties"]["power"] in filterterms:
        newfile["features"].append(file["features"][i])
    else:
        ignoredItems += 1
        print(file["features"][i]["properties"]["power"])


print("ignored "+ str(ignoredItems) + "items of " +  str(len(file["features"])))
with open('powerfiltered2.json', 'w') as outfile:
    json.dump(newfile, outfile)