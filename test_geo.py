from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()

def test_stations_within_radius():
    assert len(stations_within_radius(stations, (52.2053, 0.1218), 0)) == 0
    assert len(stations_within_radius(stations, (52.2053, 0.1218), 10)) > 0
    assert len(stations_within_radius(stations, (52.2053, 0.1218), 1000)) > len(stations_within_radius(stations, (52.2053, 0.1218), 10))

