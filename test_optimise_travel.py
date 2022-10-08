# Unit tests (pytest)

import optimise_travel
import math
import pytest

def test_all_indices_present():
    coordinates = [(0,0) for i in range(314)]
    indices = optimise_travel.optimise_travel_order(coordinates)
    assert len(indices) == len(coordinates)
    assert len(set(indices)) == len(coordinates)

def test_case_1():
    coordinates = [
        (-36.932197, 174.987783),
        (-36.969210, 174.912630),
        (-37.008773, 174.835551),
        (-36.812159, 174.782783),
        (-36.987639, 174.850803),
        (-36.987525, 174.756794)
    ]
    indices = optimise_travel.optimise_travel_order(coordinates)
    coordinates_xy = optimise_travel.convert_to_utm_xy(coordinates)
    total_distance = optimise_travel.calc_total_distance(coordinates_xy, indices)
    assert len(indices) == len(coordinates)
    assert total_distance <= 43434
    
def test_case_2():
    coordinates = [
        (-38.444208, 175.821467),
        (-37.103197, 174.877639),
        (-36.771995, 174.582458),
        (-37.189848, 174.921181),
        (-37.788692, 175.221970),
        (-37.027575, 174.997799),
        (-38.131145, 176.166297),
        (-36.303898, 174.523462),
        (-37.548307, 175.711875),
        (-38.660265, 176.032597),
        (-37.008849, 174.832011),
        (-36.898576, 174.593211),
        (-37.279678, 175.374855),
        (-36.998122, 175.037219),
        (-36.701624, 174.725347)
    ]
    indices = optimise_travel.optimise_travel_order(coordinates)
    coordinates_xy = optimise_travel.convert_to_utm_xy(coordinates)
    total_distance = optimise_travel.calc_total_distance(coordinates_xy, indices)
    assert len(indices) == len(coordinates)
    assert total_distance <= 530828
    
def test_case_3():
    coordinates = [
        (-37.193432, 175.120565),
        (-38.444208, 175.821467),
        (-37.103197, 174.877639),
        (-36.771995, 174.582458),
        (-36.932197, 174.987783),
        (-36.969210, 174.912630),
        (-37.008773, 174.835551),
        (-36.812159, 174.782783),
        (-36.987639, 174.850803),
        (-36.987525, 174.756794),
        (-37.189848, 174.921181),
        (-37.788692, 175.221970),
        (-37.027575, 174.997799),
        (-38.131145, 176.166297),
        (-36.303898, 174.523462),
        (-37.548307, 175.711875),
        (-38.660265, 176.032597),
        (-37.008849, 174.832011),
        (-36.898576, 174.593211),
        (-37.279678, 175.374855),
        (-36.998122, 175.037219),
        (-36.701624, 174.725347)
    ]
    indices = optimise_travel.optimise_travel_order(coordinates)
    coordinates_xy = optimise_travel.convert_to_utm_xy(coordinates)
    total_distance = optimise_travel.calc_total_distance(coordinates_xy, indices)
    assert len(indices) == len(coordinates)
    assert total_distance <= 653027
    
def test_case_4():
    coordinates = [
        (-36.771995, 174.582458),
        (-36.812159, 174.782783),
        (-39.191610, 175.301580),
        (-39.192170, 175.303150),
        (-45.007110, 168.535670),
        (-39.141770, 175.336700),
        (-36.998122, 175.037219),
        (-38.444208, 175.821467),
        (-39.192170, 175.303150),
        (-39.141160, 175.335290),
        (-45.210870, 167.544770),
        (-39.191610, 175.301580),
        (-38.660265, 176.032597),
        (-39.166670, 175.366260),
        (-37.548307, 175.711875),
        (-36.932197, 174.987783),
        (-44.507240, 168.410540),
        (-36.303898, 174.523462),
        (-37.008849, 174.832011),
        (-37.008773, 174.835551),
        (-41.334930, 172.324010),
        (-45.253580, 167.208000),
        (-36.969210, 174.912630),
        (-37.027575, 174.997799),
        (-39.166670, 175.366260),
        (-36.701624, 174.725347),
        (-45.034680, 168.484120),
        (-45.297550, 167.401590),
        (-45.189700, 168.107440),
        (-38.131145, 176.166297),
        (-36.987639, 174.850803),
        (-45.295670, 167.418970),
        (-41.268610, 175.146740),
        (-45.199680, 168.104040),
        (-40.534560, 172.306540),
        (-37.103197, 174.877639),
        (-37.189848, 174.921181),
        (-44.404170, 168.204570),
        (-37.788692, 175.221970),
        (-36.898576, 174.593211),
        (-37.193432, 175.120565),
        (-37.279678, 175.374855),
        (-39.141140, 175.335220),
        (-36.987525, 174.756794),
        (-39.141770, 175.336700)
    ]
    indices = optimise_travel.optimise_travel_order(coordinates)
    coordinates_xy = optimise_travel.convert_to_utm_xy(coordinates)
    total_distance = optimise_travel.calc_total_distance(coordinates_xy, indices)
    assert len(indices) == len(coordinates)
    assert total_distance <= 8070152
    