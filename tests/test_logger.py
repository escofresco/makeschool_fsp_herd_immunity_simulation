import os
import unittest
from person import Person
from logger import Logger
from virus import Virus


class TestSuite(unittest.TestCase):

    def setUp(self):
        self.test_file_name = "test.txt"
        self.test_file_path = "./logs/"+self.test_file_name

    # def tearDown(self):
    #     os.remove("logs/"+self.test_file_name)

    def remove_test_file(self):
        os.remove(self.test_file_path)

    def test_logger_initialization(self):
        with Logger(self.test_file_name) as logger:
            self.assertEqual(logger.file_name, self.test_file_name)
        self.remove_test_file()

    def test_writes_metadata_to_new_file(self):
        params = [100, 0.5, "big v", 0.9, 10]
        with Logger(self.test_file_name) as logger:
            logger.write_metadata(*params)
        with open(self.test_file_path, 'r') as test_file:
            self.assertEqual(test_file.readline(), "\t".join(map(str, params))+"\n")
        self.remove_test_file()

    def test_writes_metadata_to_existing_file(self):
        pass

    def test_infection_survival_did_not_survive_is_logged(self):
        person2 = Person(7, True)
        with Logger(self.test_file_name) as logger:
            logger.log_interaction(random_already_sick_person,
                                             random_unvax_person,
                                             did_infect=True)
        with open(self.test_file_path, 'r') as test_file:
            last_line = test_file.readline()
            self.assertEqual(
                last_line,
                f"{random_already_sick_person._id} infects {random_unvax_person._id}.\n",
            )
        self.remove_test_file()

    def test_interaction_is_logged_unsuccessful_infection_because_of_vaccination(
            self):
        random_vax_person = Person(5, True)
        eboola = Virus("Eboola", 0.7, 0.9)
        random_already_sick_person = Person(6, False, eboola)
        with Logger(self.test_file_name) as logger:
            logger.log_interaction(random_already_sick_person,
                                             random_vax_person,
                                             did_infect=False)
        with open(self.test_file_path, 'r') as test_file:
            last_line = test_file.readline()
            self.assertEqual(
                last_line,
                f"{random_already_sick_person._id} infects {random_vax_person._id}.\n",
            )
        self.remove_test_file()

    def test_interaction_is_logged_unsuccessful_infection_because_already_sick(
            self):
        eboola = Virus("Eboola", 0.7, 0.9)
        person1 = Person(4, False, eboola)
        random_already_sick_person = Person(6, False, eboola)
        with Logger(self.test_file_name) as logger:
                logger.log_interaction(person1,
                                                 random_already_sick_person,
                                                 did_infect=False)
        with open(self.test_file_path, 'r') as test_file:
            last_line = test_file.readline()
            self.assertEqual(
                last_line,
                f"{person1._id} infects {random_already_sick_person._id}.\n")
        self.remove_test_file()

    def test_infection_survival_is_logged(self):
        person2 = Person(7, True)
        with Logger(self.test_file_name) as logger:
            logger.log_infection_survival(person2, False)
        with open(self.test_file_path, 'r') as test_file:
            last_line = test_file.readline()
            self.assertEqual(last_line, f"{person2._id} survived infection.\n")
        self.remove_test_file()

    def test_infection_survival_did_not_survive_is_logged(self):
        person2 = Person(7, True)
        with Logger(self.test_file_name) as logger:
            logger.log_infection_survival(person2, True)
        with open(self.test_file_path, 'r') as test_file:
            last_line = test_file.readline()
            self.assertEqual(last_line, f"{person2._id} died from infection.\n")
        self.remove_test_file()

    def test_time_step(self):
        pass


if __name__ == "__main__":
    unittest.main()
