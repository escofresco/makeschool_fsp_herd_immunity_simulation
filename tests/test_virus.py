import unittest

from virus import Virus


class TestSuite(unittest.TestCase):

    def test_virus_init_method(self):
        name = "big cough"
        repro_rate = 0.99
        mortality_rate = 0.98
        virus = Virus(name, repro_rate, mortality_rate)
        self.assertEqual(virus.name, name)
        self.assertEqual(virus.repro_rate, repro_rate)
        self.assertEqual(virus.mortality_rate, mortality_rate)


if __name__ == "__main__":
    unittest.main()
