"""Flood Submodule"""
#from curses.ascii import NUL
import string
from turtle import st
from unittest import skip
import numpy as np

from floodsystem.geo import stations_by_river
from .utils import sorted_by_key  # noqa

from .station import MonitoringStation


from floodsystem.stationdata import build_station_list, update_water_levels


def stations_highest_rel_level(stations, N):
     """
    Function that returns the N number of most at risk stations.
    Args:
        stations (list): List of stations (MonitoringStation).
        N (int): Length of the desired list
    Returns:
        list: List of stations (MonitoringStation).
    """
     return sorted(filter(
        lambda x: x.relative_water_level() is not None,
        stations
    ),
        key=lambda x: x.relative_water_level(),
        reverse=True
    )[:N] 


def stations_highest_rel_level_wrong(stations, N):
    """stations_highest_rel_level_wrong(stations, N) returns a list of N stations in which the water level is closest to the maximum"""
    difference = []
    if stations[0].latest_level == None:
        update_water_levels(stations)

    for station in stations:
        if station.typical_range_consistent():
            try:
                if (station.latest_level - station.typical_range[1]) < 50:
                    difference.append((station.name, (station.latest_level - station.typical_range[1])))

            except Exception:
                difference.append((station.name, -5000))
                # if station.latest_level == None
        else:
            difference.append((station.name, -5000))

    difference = sorted(difference, key=lambda x: -x[1])
    #print(difference)
    return difference[:N]



def stations_level_over_threshold(stations, tol):
    """
    Function that returns stations whose latest relative water level is over some threshold.
    Args:
        stations (list): List of stations (MonitoringStation).
        tol (float): The threshold relative water level.
    Returns:
        list: List of tuples in the format (station (MonitoringStation),
        relative water level) sorted by the relative level in descending order.
    """

    return sorted_by_key(filter(
        lambda x: x[1] > tol,
        [(station, station.relative_water_level()) for station in stations if
         station.relative_water_level() is not None]
    ), 1, reverse=True)