# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""


import imp
from floodsystem.stationdata import update_water_levels


def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)


from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels

#function for 2F which sorts the stations by the current river levels 
def sort_by_current_levels(stations):

  update_water_levels(stations)

  #creating an empty list for the names of the reivers and the levels 
  names = []
  levels = []

  #Adding the names of the stations to the list and also the stations latest water levels to the list 
  for station in stations:
      names.append(station.name)
      levels.append(station.latest_level)

  #forming a series of tuples of the names and water levels  
  tuple = list(zip(names, levels))

  #
  for i in range(len(tuple)):
      if tuple[i][1] == None:
          tuple[i] = ('', 0)
  
  #sorting 
  tuple = sorted_by_key(tuple, 1)
  

  return(tuple)
