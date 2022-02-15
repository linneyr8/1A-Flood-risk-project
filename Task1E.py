#determining the N rivers with the greatest number of monitoring stations

# from floodsystem.geo import rivers_with_station
# From floodstystem.geo import stations_by_river 
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list 


if __name__ == "__main__":
    print("*** Task 1E: CUED Part 1A Flood Warning System ***")

    stations = build_station_list()
    N = 9
    station_number = rivers_by_station_number(stations, N)

    print(station_number)