from distutils.command.build import build
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
        stations= build_station_list()

        output= rivers_with_station(stations)
        print(len(output))
        print(output[0:10])

        river_dictionary = stations_by_river(stations)

        print(river_dictionary["River Aire"])
        print(river_dictionary["River Cam"])
        print(river_dictionary["River Thames"])
if __name__ == "__main__":
    print("*** Task 1D: CUED Part 1A Flood Warning System ***") 
    run()  
