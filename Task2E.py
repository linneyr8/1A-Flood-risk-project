from matplotlib.pyplot import show
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import numpy as np
from bokeh.io import show
from datetime import timedelta


def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_risk_stations = stations_highest_rel_level(stations, 5)
    for high_risk_station in high_risk_stations:
        dates, levels = fetch_measure_levels(high_risk_station.measure_id, dt=timedelta(days=10))
        plot_water_levels(high_risk_station, dates, levels)
    


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()