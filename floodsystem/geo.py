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
    #build list
    # stations = build_station_list()
    names = []
    distance = []
    #build list of (name, distance)
    for station in stations:
        names.append(station.name)
        distance.append(haversine(p, station.coord))
    tuples = list(zip(names, distance))
    tuples = sorted_by_key(tuples,1)
    return tuples

def stations_within_radius(stations, centre, r):
    #build list
    # stations = build_station_list()
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
    """
    Function that, given a list of station objects,
    returns a container with the names of the rivers with a monitoring station.
    
    Args:
        stations (list): List of stations (MonitoringStation).
    
    Returns:
        set: Set of names of rivers with a monitoring station.
    """

    return {station.river for station in stations}

def rivers_by_station_number(stations, N):
    """rivers_by_station returns the sorted list of tuples of the names of rivers and number of stations """
    top_list = []
    river_dict = stations_by_river(stations)
    
    station_number = []
    river_key = list(river_dict.keys())
    for river in river_dict:
        station_number.append(len(river_dict[river]))

    bob = list(zip(river_key, station_number))
    bob.sort(key = lambda x:x[1])
    while bob[len(bob)-N][1] == bob[len(bob)-(N+1)][1]:
        N = N+1

    top_list = bob[len(bob)-N:len(bob)]

    return top_list
    
    
    
     
    
    


