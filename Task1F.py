#Identifying stations which have inconsitent data for typical high/low ranges (i).no data is available (ii).the typical high range is < typical low range reported

from cProfile import label
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations 
from floodsystem.station import MonitoringStation 
stations = build_station_list 


def run():
    # Add a fake station to test the consitency with typical range wrong way round
    fake_station = MonitoringStation(
        station_id= "Fake Station",
        measure_id= "hello",
        label="Fake Station",
        coord=(float(51), float(52)),
        typical_range=(float(52), float(12)),
        river="river",
        town= "town")

    stations.append(fake_station)

    inconsistent_stations= inconsistent_typical_range_stations(stations)

    inconsistent_station_names = []
    for station in inconsistent_stations:
        inconsistent_station_names.append(station.name)
    inconsistent_station_names = sorted(inconsistent_station_names)

    print(inconsistent_station_names)
if __name__ == "__main__":
    print("*** Task 1F: CUED Part 1A Flood Warning System ***") 
    run()  
