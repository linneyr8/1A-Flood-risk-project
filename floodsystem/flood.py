from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    # Returns stations whose latest relative water level is over some threshold.
    # list is sorted by relative level in descending order
    return sorted_by_key(filter(
        lambda x: x[1] > tol,
        [(station, station.relative_water_level()) for station in stations if station.relative_water_level() is not None]
    ), 1, reverse=True)

def stations_highest_rel_level(stations, N):
    return sorted(filter(
        lambda x: x.relative_water_level() is not None,
        stations
    ),
        key=lambda x: x.relative_water_level(),
        reverse=True
    )[:N]