from collections import namedtuple
from functools import wraps
import unittest

from logger import Logger
from person import Person
from virus import Virus
from simulation import Simulation


def many_objects(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        VirusArgs = namedtuple("VirusArgs", "name repro_rate mortality_rate")
        SimulationArgs = namedtuple(
            "SimulationArgs",
            "pop_size vacc_percentage virus logger initial_infected")
        virus_args_tuples = [
            VirusArgs("earth", 1, 0),
            VirusArgs("wind", 0, 1),
            VirusArgs("fire", .5, .25),
            VirusArgs("big earth", .25, .75),
        ]
        with Logger("sim_test_log.txt") as logger:
            simulation_args_list = [[100, .1, None, logger, 50],
                                    [100000, 0, None, logger, 1000],
                                    [100000, .9, None, logger, 100],
                                    [100, .5, None, logger, 1],
                                    [100, .5, None, logger, 50],
                                    [100, .5, None, logger, 49],
                                    [2, .5, None, logger, 0]]

            for simulation_args in simulation_args_list:
                for virus_args_tuple in virus_args_tuples:
                    virus = Virus(*virus_args_tuple._asdict().values())
                    simulation_args[2] = virus
                    simulation_args_tuple = SimulationArgs(*simulation_args)
                    simulation = Simulation(
                        *simulation_args_tuple._asdict().values())
                    func(
                        self, {
                            "virus": virus,
                            "virus_args_tuples": virus_args_tuple,
                            "simulation": simulation,
                            "simulation_args_tuple": simulation_args_tuple
                        })

    return wrapper


class TestSuite(unittest.TestCase):

    @many_objects
    def test_initialization(self, kwargs):
        for i, (k, v) in enumerate(
                kwargs["simulation_args_tuple"]._asdict().items()):
            with self.subTest(i=i):
                # For each subtest, compare the value passed to the simulation
                # object and the corresponding instance variable in simulation
                self.assertEqual(kwargs["simulation"].__dict__[k], v)

    def test_newly_infected(self):
        pass

    @many_objects
    def test_create_population(self, kwargs):
        population = kwargs["simulation"]._create_population(
            kwargs["simulation_args_tuple"].initial_infected)
        result_infected_person_count = 0
        result_vaccinated_person_count = 0
        expected_infected_person_count = kwargs[
            "simulation_args_tuple"].initial_infected
        expected_vaccinated_person_count = (
            kwargs["simulation"].vacc_percentage *
            kwargs["simulation_args_tuple"].pop_size)
        for person in population:
            result_infected_person_count += 1 if person.infection else 0
            result_vaccinated_person_count += person.is_vaccinated
        self.assertEqual(result_infected_person_count,
                         expected_infected_person_count)
        self.assertEqual(result_vaccinated_person_count,
                         expected_vaccinated_person_count)

    # @many_objects
    # def test_
