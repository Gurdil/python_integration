__author__ = 'philip_j'

from . import Station


class Antenna:
    """
        The antenna of the station
    """

    def __init__(self, station=Station()):
        """
        The constructor

        @param station: The station were the antenna is linked
        @type station: L{Station<Station>}

        """
        self.station = Station()

    def add(self, a=5, b=-1):
        """
        simple add

        @param a: first arg
        @type a: int
        @param b: second arg
        @type b: int
        @rtype: int
        @return: this method return the value a+b+1

        @note:

            >>> Antenna().add(1, 1)
            3

        @see: L{station<Station>}

        """
        c = 1
        return a + b + c
