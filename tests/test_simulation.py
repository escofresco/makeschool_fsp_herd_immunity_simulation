import unittest
from person import Person
from virus import Virus
from simulation import Simulation


class TestSuite(unittest.TestCase):

    def setUp(self):
        self.virus = Virus("big V", 0.5, 0.75)
        self.norm_simulation = Simulation(100, 0.1, self.virus)

    def test_newly_infected(self):
        self.person = Person(6, False, self.virus)
        self.person = Person(7, False, self.virus)

    def test_create_population(self):
        population = self.norm_simulation._create_population(
            self.norm_simulation.initial_infected)
        vaccinated_person_count = 0
        infected_person_count = 0
        for person in population:
            vaccinated_person_count += int(person.is_vaccinated)
            infected_person_count += 1 if person.infection else 0
        self.assertEqual(
            vaccinated_person_count, self.norm_simulation.vacc_percentage *
            self.norm_simulation.pop_size)
        self.assertEqual(infected_person_count,
                         self.norm_simulation.initial_infected)

    def 
