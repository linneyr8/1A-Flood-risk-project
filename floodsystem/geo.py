# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
from . import datafetcher
from .station import MonitoringStation
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
    stations = build_station_list()
    names = []
    distance = []
    for station in stations:
        names.append(station.name)
        distance.append(haversine(p, station.coord))
    tuples = list(zip(names, distance))
    tuples = sorted_by_key(tuples,1)
    return tuples

def stations_within_radius(stations, centre, r):
    stations = build_station_list()
    names = []
    for station in stations:
        if haversine(centre, station.coord) <= r:
            names.append(station.name)
        else:
            pass
    return names

def stations_by_river(stations):
    """stations_by_river returns the dictionary of rivers --the key-- and the sorted list of station names"""
    dictionary = {}
    for station in stations:
        if not station.river in dictionary:
            dictionary.update({station.river: list([station.name])})
            
        else:
            dictionary[station.river]=list(dictionary[station.river]) + [station.name]
    
    for station in dictionary:
        dictionary[station] = sorted(dictionary[station])
        #sort the names in the lists for all rivers

    return dictionary

def rivers_with_station(stations):
    """rivers_with_station returns the names of rivers with a monitoring station without repeats"""
    stationsRivers = set()
    for station in stations:
        stationsRivers.add(station.rivers)
    stationRivers = sorted(stationsRivers)
    return stationRivers 

def rivers_by_station_number(stations, N):
    """rivers_by_station returns the sorted list of tuples of the names of rivers and number of stations """

    stations_by_riv = stations_by_river(stations) 

    #create empty list of rivers
    rivers_stations = []

    #add number of stations to list
    for key, value in stations_by_riv.items():
        rivers_stations.append((key, len(value)))

    #sort list by number of stations
    rivers_stations = sorted(rivers_stations, key = lambda x:-x[1])  

    output = rivers_stations[:N]

    #sort what happens if nth entry has equal sumber of stations
    list_complete = False
    while list_complete == False:
        if rivers_stations[N][1] == rivers_stations[N+1][1]:
            output.append(rivers_stations[N+1])
            
        else:
            list_complete = True

<<<<<<< HEAD
    return output
=======
    return output

>>>>>>> 5b3574733a39c8e9e01033fc2d6b9aeac79d6c84
