import unittest

from virus import Virus
from simulation import Simulation

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.virus = Virus("big V", .5, .75)
        self.norm_simulation = Simulation(100, .1, self.virus)

    def test_newly_infected(self):
        pass

    def test_create_population(self):
        pass
