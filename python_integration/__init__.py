"""
Main package
"""

__author__ = 'philip_j'
__all__ = ['Station', 'Satellite', 'lol', 'show']
__version__ = "1.0"
from python_integration.ground import Station
from python_integration.space import Satellite
from python_integration.util import Speaking as lol
from python_integration.main import show
