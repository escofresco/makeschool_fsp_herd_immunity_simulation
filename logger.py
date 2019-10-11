import os


class Logger(object):

    def __init__(self, file_name, log_dir="logs"):
        self.file_name = file_name
        self.log_dir = "./" + log_dir.strip("/") + "/"
        self.file_path = self.log_dir + self.file_name

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def __enter__(self):
        self.log_file = open(self.file_path, "w+")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.log_file:
            self.log_file.close()

    def write_metadata(self, pop_size, vacc_percentage, virus_name,
                       mortality_rate, basic_repro_num):
        """The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file."""
        self.log_file.write("\t".join([
            "pop_size", "vacc_percentage", "virus_name", "mortality_rate",
            "basic_repro_num"
        ]) + "\n")
        self.log_file.write("\t".join(
            map(str, [
                pop_size,
                vacc_percentage,
                virus_name,
                mortality_rate,
                basic_repro_num,
            ])) + "\n")

    def log_interaction(self,
                        person,
                        random_person,
                        random_person_sick=None,
                        random_person_vacc=None,
                        did_infect=None):
        '''The Simulation object should use this method to log every interaction
        a sick person has during each time step
        The format of the log should be: "{person.ID} infects {random_person.ID} \n"
        or the other edge cases:
        "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'}\n"'''

        if person.is_vaccinated:
            self.log_file.write(
                f"{person._id} didn't infect {random_person._id} because {person.is_vaccinated or 'already sick'}.\n"
            )
        else:
            self.log_file.write(f"{person._id} infects {random_person._id}.\n")

    def log_infection_survival(self, person, did_die_from_infection):
        """ The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        """
        self.log_file.write(
            f"{person._id} {'died from' if did_die_from_infection else 'survived'} infection.\n"
        )

    def log_time_step(self, time_step_number):
        """ STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        """
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass
