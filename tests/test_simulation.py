import unittest

from virus import Virus
from simulation import Simulation


class TestSuite(unittest.TestCase):

    def setUp(self):
        self.virus = Virus("big V", 0.5, 0.75)
        self.norm_simulation = Simulation(100, 0.1, self.virus)

    def test_newly_infected(self):
        pass

    def test_create_population(self):
        pass
