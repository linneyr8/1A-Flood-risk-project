from matplotlib.pyplot import show
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import numpy as np
from bokeh.io import show


def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_risk_stations = stations_highest_rel_level(stations, 5)

    p = plot_water_levels(high_risk_stations, dt=10)
    show(p)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()