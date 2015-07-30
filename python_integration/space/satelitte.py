__author__ = 'philip_j'
__all__ = ['Satellite']

from ..util import Speaking


class Satellite(Speaking):
    """
    Representation of a satellite
    """

    def __init__(self):
        self.name = "G01"
        """
        @ivar: The name of the Sat
        @type: String
        """
