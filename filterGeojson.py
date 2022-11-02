import json

f = open("aerialways_alps.geojson",encoding="utf8")
print(f)
file = json.load(f)
ignoredItems = 0
newfile = {}
newfile["type"] = "FeatureCollection"
newfile["name"] = file["name"] + "f"
newfile["crs"] = file["crs"]
newfile["features"] = []

filterterms= ["magic_carpet","platter","rope_tow","t-bar","drag_lift","station","pylon","j-bar","proposed"]
 

for i in range (len(file["features"])):

    
   
    if file["features"][i][ "properties"]["aerialway"] in filterterms:
        ignoredItems += 1
    else:

        

        newfile["features"].append(file["features"][i])
        print(file["features"][i][ "properties"]["aerialway"])

print("ignored "+ str(ignoredItems) + "items of " +  str(len(file["features"])))
#with open('pfile.json', 'w') as outfile:
    #json.dump(newfile, outfile)