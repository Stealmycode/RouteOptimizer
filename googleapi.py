import googlemaps
from itertools import permutations
from config import apikey

gmaps = googlemaps.Client(key=apikey)
origins = [  
    "Alabama",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Utah",
    "Maine",
    ]
destinations = origins
matrix = gmaps.distance_matrix(origins, destinations)
print(matrix["rows"])
myMatrix = []
for i in range(len(origins)):
    myRow = []
    for j in range(len(destinations)):
        travelTime = matrix["rows"][i]["elements"][j]["duration"]["value"]
        myRow.append(travelTime)
    myMatrix.append(myRow)

print(myMatrix)
paths = list(permutations(range(len(origins))))
print(len(paths))
optimalPath = [(0,1),999999999999]
for i in range(len(paths)):
    route = paths[i]
    travelTime = 0
    for j in range(len(route)-1):
        travelTime += myMatrix[route[j]][route[j+1]]
    if travelTime < optimalPath[1]:
        optimalPath = [paths[i],travelTime]
print(optimalPath)
addresses = [origins[i] for i in optimalPath[0]]
print(addresses)