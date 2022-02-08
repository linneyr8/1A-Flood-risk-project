#Identifying stations which have inconsitent data for typical high/low ranges (i).no data is available (ii).the typical high range is < typical low range reported

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations 


def run():
    stations = build_station_list() 
    inconsistent_stations= inconsistent_typical_range_stations(stations)

    print(inconsistent_stations)
    
if __name__ == "__main__":
    print("*** Task 1F: CUED Part 1A Flood Warning System ***") 
    run()
