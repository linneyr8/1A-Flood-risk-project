from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

stations = build_station_list()
radius = 10
p = (52.2053, 0.1218)

def test_stations_within_radius():
    fake_station1 = MonitoringStation(
        station_id = "fs1",
        measure_id = "gg",
        label = "fs1",
        coord = (52.203, 0.0122),
        typical_range = (10, 20),
        river = "r1",
        town = "t1")
    fake_station2 = MonitoringStation(
        station_id = "fs2",
        measure_id = "gg",
        label = "fs2",
        coord = (52.21, 0.123),
        typical_range = (52.21, 0.123),
        river = "r2",
        town = "t2")
    fake_station3 = MonitoringStation(
        station_id = "fs3",
        measure_id = "gg",
        label = "fs3",
        coord = (60.1282, 18.6435),
        typical_range = (1, 19),
        river = "r3",
        town = "t3")
    
    test_stations = (fake_station1, fake_station2, fake_station3)
    expected_s = ("fs1", "fs2")
    assert expected_s == stations_within_radius(test_stations, p, radius)