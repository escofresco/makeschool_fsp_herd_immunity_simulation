import unittest

from person import Person
from virus import Virus

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
        self.assertEqual(person._id, 2)
        self.assertFalse(person.is_vaccinated)
        self.assertEqual(person.infection, None)




    def test_sick_person_instantiation(self):
        # Create a Virus object to give a Person object an infection
        virus = Virus("Dysentery", 0.7, 0.2)
        # Create a Person object and give them the virus infection
        person = Person(3, False, virus)
        self.assertEqual(person.is_vaccinated, True)
        self.assertTrue(person.is_alive)
        self.assertEqual(person._id, 3)
        self.assertEqual(person.infection, virus)


    def test_did_survive_infection(self):
        virus = Virus("Dysentery", 0.7, 0.2)
        person = Person(4, False, virus)

        # Resolve whether the Person survives the infection or not
        survived = person.did_survive_infection()
        # Check if the Person survived or not
        if survived:
            self.assertTrue(person.is_alive)
            self.assertTrue(person.is_vaccinated)
        else:
            self.assertFalse(person.is_alive)
            self.assertFalse(person.is_vaccinated)


if __name__ == "__main__":
    unittest.main()
