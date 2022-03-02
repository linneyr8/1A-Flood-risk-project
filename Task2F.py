from floodsystem.stationdata import build_station_list
from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels, plot_water_with_levels
from floodsystem.utils import sort_by_current_levels

#setting up list of stations 
stations = build_station_list()

#sorting the stations into the current water levels 
tuple = sort_by_current_levels(stations)

#assigning a tempoary station with null value 
temp_station = None

#prints the graphs of the stations with the highest water levels in real time 
for i in range(5):
  for station in stations:                          #iterates through the top 5 stations 
        if tuple[i][0] == station.name:           
        
            temp_station = station                 #tempoary station = to new station name with highest water level 
            dates, levels = fetch_measure_levels(temp_station.measure_id, timedelta(days = 2))   #data from the past two days 
            plot_water_with_levels(temp_station, dates, levels, 4)   #polynomial with highest power 4
