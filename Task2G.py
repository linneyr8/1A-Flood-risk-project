import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from floodsystem.analysis import polyfit


def plot_risk(stations):
    Low = 0                                                  
    Moderate = 0
    High = 0 
    Severe = 0
    for station in stations:
        if station.risk == 'Low':                           #determining if the two objects are equal
            Low += 1                                        # if it is then assign the value low to that station
        elif station.risk == 'Moderate':
            Moderate += 1
        elif station.risk == 'High':
            High += 1
        elif station.risk == 'Severe':
            Severe += 1
    
    #creating array of the risks to later implement in the x axis  
    x_pos = np.arange(4)
    Risk = ('Low', 'Moderate', 'High', 'Severe')
    Values = (Low, Moderate, High, Severe)

    #setting up the x cordinates then y cordinates of the bar graph
    plt.bar(x_pos, Values, align='center')

    #setting up the current tick locations and labels of the x-axis 
    plt.xticks(x_pos, Risk, rotation=45)
    
    #labelling the x and y axis -- X axis= is level of risk -- Y axis is the number of stations 
    plt.xlabel('Risk')
    plt.ylabel('Number of Stations')

    #printing just the values/points which would of been plotted on the graph 
    plt.show()

