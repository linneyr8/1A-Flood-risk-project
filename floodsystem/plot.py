from datetime import timedelta
from os import environ

import numpy as np


def plot_water_levels(station, dates, levels):
    output_file(station.name + ".html")
    p = figure(title = station.name, x_axis_label = "Date", y_axis_label = "Water Level (m)", active_scroll = "wheel_zoom")
    p.lines(dates, levels, line_width = 1)
    p.xaxis.formatter = DatetimeTickFormatter(
        hours = ["%d %B %Y"],
        days = ["%d %B %Y"],
        months = ["%d %B %Y"],
        years = ["%d %B %Y"],)
    p.xaxis.major_label_orientation = np.pi / 4
    return p