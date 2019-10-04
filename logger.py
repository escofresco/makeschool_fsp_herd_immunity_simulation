class Logger(object):
    def __init__(self, file_name, log_dir="logs"):
        self.file_name = file_name
        self.log_dir = './'+log_dir.strip('/')+'/'

    def __enter__(self):
        self.log_file = open(self.self.file, 'a')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log_file.close()

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num

        '''The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.'''
        temp_file.write('\t'.join([self.pop_size,
                                   self.vacc_percentage,
                                   self.virus_name,
                                   self.mortality_rate,
                                   self.basic_repro_num]))

    def log_interaction(self, person, random_person, random_person_sick=None, random_person_vacc=None, did_infect=None):
        self.person = person
        self.random_person = random_person
        self.random_person_sick = random_person_sick
        self.random_person_vacc = random_person_vacc
        self.did_infect = did_infect

        '''The Simulation object should use this method to log every interaction
        a sick person has during each time step
        The format of the log should be: "{person.ID} infects {random_person.ID} \n"
        or the other edge cases:
        "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"'''

        if self.person.is_vaccinated:
            print(f"{person._id} didn't infect {random_person._id} because {person.is_vaccinated or 'already sick'} \n")
        else:
            print(f"{person._id} infects {random_person._id} \n")

    def log_infection_survival(self, person, did_die_from_infection):
        self.person = person
        self.did_die_from_infection = did_die_from_infection

        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile


    def resolve_infection(self):
        # if person survives infection print()
        if self.did_die_from_infection:
            print(f"{self.person.ID} died from infection\n" or f"{self.person.ID} survived infection. \n")
        else:
            print(f"{self.person.ID} survived infection. \n")
        pass

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass
