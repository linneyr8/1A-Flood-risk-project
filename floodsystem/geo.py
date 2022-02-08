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
    stations = build_station_list()
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
    
    name_of_rivers = set()  #so no repeats of the names of rivers occurr
    name_n_num = []  #unsorted
    name_n_num_1 = [] #sorted
    name_n_num_N = [] #final list with repitiion check
    n=0 #number of stations count
    
    for names in stations:
        name_of_rivers.add(names.river)
        
    for river in name_of_rivers:
        for object in stations:
            if river == object.river:
                n += 1
            name_n_num.append((river,n))
            n=0 
            
    name_n_num_1 = sorted_by_key(name_n_num, 1, reverse=true)
    
    temp_0 = name_n_num_1[N]
    temp_1 = []
    for i in range(0, N-1):
        temp_1.append(name_n_num_1[i])
    [temp_1.append(item) for item in name_n_num_1 if item[1]]
    
    [name_n_num_N.append(j) for j in temp_1 if j not in name_n_num_N]
    
    return name_n_num_N
    
    
     
    
    


