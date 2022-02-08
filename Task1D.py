from distutils.command.build import build
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
        """"
        Print how many rivers have at least one monitoring station
        prints the first 10 of these rivers in alphabetical order
        print the names of the stations located on the following rivers in alhabetical order
           'River Aire'
           'River Cam'
           'River Thames'
         """
        stations= build_station_list()
        rivers = rivers_with_station(stations)

        print(len(rivers))
        print(sorted(rivers)[:10])

        stations_on_river = stations_by_river(stations)
        for river in ['River Aire', 'River Cam', 'River Thames']:
                print(rivers + ':')
                print(sorted([i.name for i in stations_on_river[rivers]]))
                
                                
if __name__ == "__main__":
    print("*** Task 1D: CUED Part 1A Flood Warning System ***") 
    run()  
