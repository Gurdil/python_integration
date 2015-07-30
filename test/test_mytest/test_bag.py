__author__ = 'philip_j'

from python_integration.ground.station import convert
from python_integration.ground.antenna import Antenna
import numpy as np


class Test_source:
    def test_convert(self):
        assert np.allclose(convert(6, 2), np.array([0, 0.00000001, 0]))

    def test_antenna(self):
        assert Antenna().add(2, 3) == 6
