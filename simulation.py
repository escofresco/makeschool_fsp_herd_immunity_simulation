from virus import Virus
from logger import Logger
from person import Person
import random
import sys
random.seed(42)


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''

    def __init__(self,
                 pop_size: int,
                 vacc_percentage: float,
                 virus: Virus,
                 initial_infected=1):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''

        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        #self.logger = Logger("logs.txt")
        # List of Person objects
        self.pop_size = pop_size    # Int
        self.next_person_id = 0    # Int
        self.virus = virus    # Virus object
        self.initial_infected = initial_infected    # Int
        self.total_infected = 0    # Int
        self.current_infected = 0    # Int
        self.vacc_percentage = vacc_percentage    # float between 0 and 1
        self.vacc_count = int(self.vacc_percentage * self.pop_size)
        self.total_dead = 0    # Int
        # self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(self.virus.name, pop_size, vacc_percentage, initial_infected)
        self.newly_infected = []
        self.population = self._create_population(pop_size)

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
        Args:
        initial_infected (int): The number of infected people that the simulation
        will begin with.

        Returns:
        list: A list of Person objects.
        '''
        people_list = []
        for infected_person in range(initial_infected):
            people_list.append(
                Person(infected_person, False, infection=self.virus))

        for self.vacc_count in range(initial_infected,
                                     initial_infected + self.vacc_count):
            people_list.append(Person(self.vacc_count, True, infection=None))

        for person in range(initial_infected + self.vacc_count, self.pop_size):
            people_list.append(Person(person, False, infection=None))
        return people_list

    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

        Returns:
        bool: True for simulation should continue, False if it should end.
        '''
        print("=" * 30)
        print(self.total_dead)
        print(self.vacc_count)
        return self.pop_size in {self.total_dead, self.vacc_count}

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method. To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.
        # call time step increment the # of times count the number

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0

        while self._simulation_should_continue():
            self.time_step()
            time_step_counter += 1
        print(f'The simulation has ended after {time_step_counter} turns.')

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.
        This includes:
        1. 100 total interactions with a randon person for each infected person
        in the population
        2. If the person is dead, grab another random person from the population.
        Since we don't interact with dead people, this does not count as an interaction.
        3. Otherwise call simulation.interaction(person, random_person) and
        increment interaction counter by 1.
        '''
        for person in self.population:
            if (person.infection == self.virus.name) and (
                    person.is_alive == True):
                interaction_counter = 0
                while interaction_counter < 100:
                    random_person_num = random.randrange(0, self.population)
                    if (self.population[random_person_num].is_alive):
                        self.interaction(person,
                                         self.population[random_person_num])
                        interaction_counter += 1
        self._infect_newly_infected()

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
        person1 (person): The initial infected person
        random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
        # random_person is vaccinated:
        #     nothing happens to random person.
        # random_person is already infected:
        #     nothing happens to random person.
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0 and 1.  If that number is smaller
        #     than repro_rate, random_person's ID should be appended to
        #     Simulation object's newly_infected array, so that their .infected
        #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.
        if not (random_person.is_vaccinated or random_person.infected):
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.newly_infected:
            person.infection = self.virus
            did_servive = person.did_survive_infection()
            self.vacc_count += did_servive
            self.total_dead += not did_servive
        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_rate = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(pop_size,
                     vacc_percentage,
                     virus,
                     initial_infected=initial_infected)

    sim.run()
