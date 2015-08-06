__author__ = 'philip_j'

from . import Station


class Antenna:
    """
        The antenna of the station
    """

    def __init__(self, station=Station()):
        """
        The constructor

        :param station: The station were the antenna is linked
        :type station: Station

        """
        self.station = Station()

    def add(self, a=5, b=-1):
        """
        simple add lolilol

        :param a: first arg
        :type a: int
        :param b: second arg
        :type b: int
        :rtype: int
        :return: this method return the value a+b+1

        :Example:


            >>> Antenna().add(1, 1)
            3

        :see: `Station`

        """
        c = 1
        return a + b + c

    def change_station(self, station):
        """
        Change the station linked to this antenna

        :param station: The new station were the antenna is linked
        :type station: Station

        """
        self.station = Station()
