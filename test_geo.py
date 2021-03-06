"""Unit test for the geo module"""

from os import path

from floodsystem.geo import *
from floodsystem.station import MonitoringStation


class TestClass:
    def test_haversine(self):
        assert haversine((0., 0.), (0., 0.)) == 0.0
        assert round(haversine((0., 0.), (1., 1.)), 2) == 157.25
        assert round(haversine((1., 1.), (0., 0.)), 2) == 157.25

    def test_stations_by_distance(self):
        station1 = MonitoringStation(station_id='test_station_id_1',
                                     measure_id='test_measure_id_1',
                                     label='Test Station 1',
                                     coord=(0., 1.),
                                     typical_range=(0., 1.),
                                     river='test_river_1',
                                     town='test_town_1')
        station2 = MonitoringStation(station_id='test_station_id_2',
                                     measure_id='test_measure_id_2',
                                     label='Test Station 2',
                                     coord=(1., 1.),
                                     typical_range=(0., 1.),
                                     river='test_river_2',
                                     town='test_town_2')
        fake_stations = [station1, station2]
        sorted_stations = stations_by_distance(fake_stations, (0., 0.))
        assert sorted_stations[0][0:2] == ('Test Station 1', haversine((0., 0.), station1.coord))
        assert sorted_stations[1][0:2] == ('Test Station 2', haversine((0., 0.), station2.coord))
        
    def test_stations_within_radius(self):
        station1 = MonitoringStation(station_id='test_station_id_1',
                                     measure_id='test_measure_id_1',
                                     label='Test Station 1',
                                     coord=(0., 1.),
                                     typical_range=(0., 1.),
                                     river='test_river_1',
                                     town='test_town_1')
        station2 = MonitoringStation(station_id='test_station_id_2',
                                     measure_id='test_measure_id_2',
                                     label='Test Station 2',
                                     coord=(1., 1.),
                                     typical_range=(0., 1.),
                                     river='test_river_2',
                                     town='test_town_2')
        station3 = MonitoringStation(station_id='test_station_id_3',
                                     measure_id='test_measure_id_3',
                                     label='Test Station 3',
                                     coord=(10., 10.),
                                     typical_range=(0., 1.),
                                     river='test_river_3',
                                     town='test_town_3')
        fake_stations = [station1, station2, station3]
        list = stations_within_radius(fake_stations, (0., 0.), 200)
        assert len(list) == 2
        assert list[0] == "Test Station 1"
        assert list[1] == "Test Station 2"

    def test_rivers_and_stations(self):
        station1 = MonitoringStation(station_id='test_station_id_1',
                                     measure_id='test_measure_id_1',
                                     label='Test Station 1',
                                     coord=(0., 1.),
                                     typical_range=(0., 1.),
                                     river='test_river_1',
                                     town='test_town_1')
        station2 = MonitoringStation(station_id='test_station_id_2',
                                     measure_id='test_measure_id_2',
                                     label='Test Station 2',
                                     coord=(1., 1.),
                                     typical_range=(0., 1.),
                                     river='test_river_2',
                                     town='test_town_2')
        station3 = MonitoringStation(station_id='test_station_id_3',
                                     measure_id='test_measure_id_3',
                                     label='Test Station 3',
                                     coord=(10., 10.),
                                     typical_range=(0., 1.),
                                     river='test_river_2',
                                     town='test_town_3')
        fake_stations = [station1, station2, station3]
        rivers = rivers_with_station(fake_stations)
        assert len(rivers) == 2
        assert 'test_river_1' in rivers
        assert 'test_river_2' in rivers

        stations_on_river = stations_by_river(fake_stations)
        assert sorted(stations_on_river['test_river_2']) == [station2.name, station3.name]
        assert stations_on_river['test_river_1'] == [station1.name]