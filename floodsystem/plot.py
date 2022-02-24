from datetime import timedelta
from os import environ

import numpy as np
import datetime
from os import environ
from .analysis import polyfit
from .datafetcher import fetch_measure_levels
import numpy as np
from bokeh.io import output_file
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool, DatetimeTickFormatter, Span, BoxAnnotation
from bokeh.plotting import figure, gmap
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from . import datafetcher

def plot_water_levels(station, dates, levels):
    
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level(m)')
    plt.xticks(rotation = 45);
    plt.title(station.name)
    plt.legend()

    plt.tight_layout()

    plt.show

def plot_water_level_with_fit(station, dates, levels, p):
    output_file(station.name + ".html")
    graph = figure(title = station.name, x_axis_label="Date", y_axis_label="Water level (m)")
    graph.line(dates, levels, line_width=2)
    poly, d0 = polyfit(dates, levels, p)
    graph.line(dates, [poly(date - d0) for date in date2num(dates)], line_width=2, line_color='orange')
    low = Span(location=station.typical_range[0], dimension='width', line_color='gray', line_dash="4 4", line_width=2)
    graph.add_layout(low)
    high = Span(location=station.typical_range[1], dimension='width', line_color='gray', line_dash="4 4", line_width=2)
    graph.add_layout(high)
    low_box = BoxAnnotation(top=station.typical_range[0], fill_alpha=0.1, fill_color='gray')
    mid_box = BoxAnnotation(bottom=station.typical_range[0], top=station.typical_range[1], fill_alpha=0.1,
                            fill_color='green')
    high_box = BoxAnnotation(bottom=station.typical_range[1], fill_alpha=0.1, fill_color='red')
    graph.add_layout(low_box)
    graph.add_layout(mid_box)
    graph.add_layout(high_box)
    graph.xaxis.formatter = DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
    )
    graph.xaxis.major_label_orientation = np.pi / 4
    return graph
    
