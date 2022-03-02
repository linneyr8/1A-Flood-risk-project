from .utils import sorted_by_key
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels

#reece code 
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

#reece code
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

#Nicole Code
def stations_highest_rel_level_wrong(stations, N):
    """stations_highest_rel_level_wrong(stations, N) returns a list of N stations in which the water level is closest to the maximum"""
    
    #creating an empty list defined as difference
    difference = []
    
    #If the stations latest water level data compared is null then run the function which attach level data contained in measure_data to stations
    if stations[0].latest_level == None:
        update_water_levels(stations)

    """if typical_range_consistent returns true if the data is consistent then find the difference between the stations latest water 
    level and its typical water level range. If the difference is less than 50 add to the empty list defined as difference which was 
    created at the start of the function"""
    for station in stations:
        if station.typical_range_consistent():
            try:
                if (station.latest_level - station.typical_range[1]) < 50:
                    difference.append((station.name, (station.latest_level - station.typical_range[1])))
                    
    """"if station.latest_level == None"""
            except Exception:
                difference.append((station.name, -5000))
                
    """Sort the list created--- by taking arg x and returning -x[1]"""
        else:
            difference.append((station.name, -5000  
    difference = sorted(difference, key=lambda x: -x[1])
                               
    """print(difference"""
    return difference[:N]


#reeces code
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
#function takes argument x and returns the item at index 1 and compares it to the tolerance value. The argument in this case is the the relative water levels of the stations if there is data available" 
    return sorted_by_key(filter(
        lambda x: x[1] > tol,
        [(station, station.relative_water_level()) for station in stations if
         station.relative_water_level() is not None]
    ), 1, reverse=True)

#nicoles code 
""" For task 2G the function that assess the flood risks """
import numpy as np

def assess_risk(stations):
    """assess_risk(stations), returns a (station.name, station risk) in order of risk """
    
    """describing an array of items--- in this case assigning station name as a string and the value as a float"""
    dtype = [('stationName', str), ('value', float)]
                               
    """computing current level risk= creating a array of data of stations of N stations in which the water level 
    is closest to the maximum. Iterating over the list of stations"""  
    current_levels = np.array(stations_highest_rel_level_wrong(stations, len(stations)+1))
    
    """1m of the water above max level has a risk of 1, 0.4 m below max has risk of 0. Trying to get rid of the offset so below o.4m of the max water level= 0"""
    levelRisk = current_levels[:, 1].astype(float)
    levelRisk = (1)/(1.4)*(levelRisk + 0.4)
                               
    """setting the risk level into an numpy array= containing data of the current water levels. 
    astype is used to change the data type of the current water levels into a string. Iterates through each of the stations"""
    levelRisk = np.array([[current_levels[i, 0].astype(str), levelRisk[i]] for i in range(len(levelRisk))])
    
    
    #relative level risk
    #relative level 1.5 risk 1, relative level 0 risk 0
    rellevels = np.array([[station.name, station.relative_water_level()/1.5] if station.relative_water_level() != None else [station.name, station.relative_water_level()] for station in stations])
    
    levelRisk = levelRisk[np.argsort(levelRisk[:,0])]
    rellevels = rellevels[np.argsort(rellevels[:,0])]

    #levelRisk = sorted(levelRisk, key=lambda x: x[0])
    #rellevels = sorted(rellevels, key=lambda x: x[0])
    #print(levelRisk.shape)
    #print(rellevels.shape)
    #print(len(stations))
    StationsAndRisk = np.empty((len(levelRisk),2), dtype=object)

    skipstationcounter = 0

    for i in range(len(levelRisk)):
        StationsAndRisk[i, 0] = levelRisk[i, 0]
        if (levelRisk[i,0] == rellevels[i+skipstationcounter,0]):
            if rellevels[i+skipstationcounter,1] != None:
                #print(levelRisk[i,1], rellevels[i,1])
                StationsAndRisk[i,1] = ((float(levelRisk[i,1]) + float(rellevels[i+skipstationcounter,1]))/2)
            else:
                StationsAndRisk[i,1] = (levelRisk[i,1])
        else:
            #print("ERROR!!! STATIONS dont match")
            #print(levelRisk[i,0], rellevels[i+skipstationcounter,0])
            #print("in position", i)

            StationsAndRisk[i,1] = levelRisk[i,1]
            skipstationcounter += 1

            while(levelRisk[i,0] != rellevels[i+skipstationcounter,0]):
                #print(levelRisk[i+skipstationcounter,0], rellevels[i,0])
                skipstationcounter += 1
            
    """returning a new array of given shape, dtype """
    output = np.empty((len(StationsAndRisk), 2), dtype=object)
    for i, value in enumerate(StationsAndRisk):
        output[i,0] = value[0]
        if float(value[1]) > 0.7:
            output[i,1] = "High"
        elif float(value[1]) > 0.4:
            output[i,1] = "Moderate"
        else:
            output[i,1] = "Low"
    
    return(output)
