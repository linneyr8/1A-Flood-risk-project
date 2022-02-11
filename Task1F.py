#Identifying stations which have inconsitent data for typical high/low ranges (i).no data is available (ii).the typical high range is < typical low range reported
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations 

stations = build_station_list() 
x = inconsistent_typical_range_stations(stations)  
print(x)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part 1A Flood Warning System ***")