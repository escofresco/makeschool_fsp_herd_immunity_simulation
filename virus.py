class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name: str, repro_rate: float, mortality_rate: float):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate
