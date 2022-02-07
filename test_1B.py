from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

radius = float(10)
p = (52.2053, 0.1218)

def test_stations_by_distance():
    fake_station1 = MonitoringStation(
        station_id = "fs1",
        measure_id = "gg",
        label = "fs1",
        coord = (float(50), float(50)),
        typical_range = (float(10), float(20)),
        river = "r1",
        town = "t1")
    fake_station2 = MonitoringStation(
        station_id = "fs2",
        measure_id = "gg",
        label = "fs2",
        coord = (float(60), float(60)),
        typical_range = (float(52.21), float(0.123)),
        river = "r2",
        town = "t2")
    fake_station3 = MonitoringStation(
        station_id = "fs3",
        measure_id = "gg",
        label = "fs3",
        coord = (float(70), float(70)),
        typical_range = (float(1), float(19)),
        river = "r3",
        town = "t3")
    test_stations = [fake_station1, fake_station2, fake_station3]

    list_1 = stations_by_distance(test_stations, p)
    assert len(list_1) == 3
    assert len(list_1[0]) == 2
    assert isinstance(list_1[0][0], MonitoringStation) is True
    assert isinstance(list_1[0][1], float) is True

    #check list is sorted
    assert list_1[0][0] == fake_station1
    assert list_1[1][0] == fake_station2
    assert list_1[2][0] == fake_station3