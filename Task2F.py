from floodsystem.stationdata import build_station_list
from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.utils import sort_by_current_levels

#setting up list of stations 
stations = build_station_list()

#sorting the stations into the current water levels 
tuple = sort_by_current_levels(stations)

#assigning a tempoary station with null value 
temp_station = None


for station in stations:
    for i in range(5):
        if tuple[i][0] == station.name:
        
            temp_station = station
            dates, levels = fetch_measure_levels(temp_station.measure_id, timedelta(days = 2))
            plot_water_level_with_fit(temp_station, dates, levels, 4)
