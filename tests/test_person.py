import unittest

from person import Person

class TestSuite(unittest.TestCase):
    ''' These are simple tests to ensure that you are instantiating your Person class correctly. '''


    def test_vacc_person_instantiation(self):
        # create some people to test if our init method works as expected
        person = Person(1, True)
        self.assertEqual(person._id, 1)
        self.assertTrue(person.is_alive)
        self.assertTrue(person.is_vaccinated)
        self.assertEqual(person.infection, None)


    def test_not_vacc_person_instantiation(self):
        person = Person(2, False)
        # TODO: complete your own assert statements that test
        # the values at each attribute
        # assert ...
        pass


    def test_sick_person_instantiation(self):
        # Create a Virus object to give a Person object an infection
        virus = Virus("Dysentery", 0.7, 0.2)
        # Create a Person object and give them the virus infection
        person = Person(3, False, virus)
        # TODO: complete your own assert statements that test
        # the values at each attribute
        # assert ...
        pass


    def test_did_survive_infection(self):
        # TODO: Create a Virus object to give a Person object an infection
        virus = Virus("Dysentery", 0.7, 0.2)
        # TODO: Create a Person object and give them the virus infection
        person = Person(4, False, virus)

        # Resolve whether the Person survives the infection or not
        survived = person.did_survive_infection()
        # Check if the Person survived or not
        if survived:
            self.assertTrue(person.is_alive)
            # TODO: Write your own assert statements that test
            # the values of each attribute for a Person who survived
            # assert ...
        else:
            self.assertFalse(person.is_alive)
            # TODO: Write your own assert statements that test
            # the values of each attribute for a Person who did not survive
            # assert ...
            pass


if __name__ == "__main__":
    unittest.main()
