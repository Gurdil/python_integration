__author__ = 'philip_j'
__all__ = ['Station']

from ..util import Speaking
import numpy as np


class Station(Speaking):
    """
        A station CORS
    """
    pass

    def lala(self):
        """
            Say lala
        """
        print('lala')


def convert(lat, long):
    """
    Convert a lattitude longitude coordonnate into ECEF

    :param lat: lattitude
    :param long: longitude
    :return: ECEF [X, Y, Z]
    """
    return np.array([0, 0, 0])
