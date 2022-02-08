#determining the N rivers with the greatest number of monitoring stations

# from floodsystem.geo import rivers_with_station
# From floodstystem.geo import stations_by_river 
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list 

#creating a tuple
print(rivers_by_station_number(build_station_list(),9))
