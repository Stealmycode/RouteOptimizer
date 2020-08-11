import googlemaps
from itertools import permutations
from config import apikey

def calculate_optimal_path(addresses):
    gmaps = googlemaps.Client(key = apikey)
    distance_matrix = gmaps.distance_matrix(addresses, addresses)
    time_matrix = []
    for i in range(len(addresses)):
        row = []
        for j in range(len(addresses)):
            travel_time = distance_matrix["rows"][i]["elements"][j]["duration"]["value"]
            row.append(travel_time)
        time_matrix.append(row)
    paths = list(permutations(range(len(addresses))))
    optimal_time = float('inf')
    optimal_path = []
    for path in paths:
        travel_time = 0
        for i in range(len(path)-1):
            travel_time += time_matrix[path[i]][path[i+1]]
        if travel_time < optimal_time:
            optimal_time = travel_time
            optimal_path = path
    address_path = [addresses[i] for i in optimal_path]
    return address_path





def main():
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

if __name__ == "__main__":
    main()