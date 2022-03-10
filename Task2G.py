import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

"""Get a list of stations in each town 
For each list of station in each town 
calculate the risk level and print """


def find_risk_level(stations):
    """returns a string of risk level"""
    if stations_highest_rel_level < 

    return """to do"""

stations= build_station_list()
dict_of_stations_in_town = dict()
for station in stations:
    if station.town in dict_of_stations_in_town:
        dict_of_stations_in_town[station.town].append(station)
    else: #if the town is already not in the dictionary
        dict_of_stations_in_town[station.town] = [station] 

for list_of_stations in dict_of_stations_in_town.values():
    print("risk level for:", list_of_stations[0].town, "is", find_risk_level(list_of_stations))
