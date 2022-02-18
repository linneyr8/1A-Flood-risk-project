from datetime import timedelta

from bokeh.io import show

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
  stations= build_station_list()
  
