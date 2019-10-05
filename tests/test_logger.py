import os
import unittest
from person import Person
from logger import Logger
from virus import Virus


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.temp_file_name = "temp_logs.txt"
        self.temp_file = open(self.temp_file_name, "w+")
        self.test_logger = Logger(self.temp_file_name)

    def tearDown(self):
        self.temp_file.close()
        os.remove(self.temp_file_name)

    def test_logger_initialization(self):
        self.assertEqual(self.test_logger.file_name, self.temp_file_name)

    def test_writes_metadata_to_new_file(self):
        file_lines = self.temp_file.readlines()
        self.assertEqual(len(file_lines), 0)

        params = [100, 0.5, "big v", 0.9, 10]
        self.test_logger.write_metadata(*params)
        self.assertEqual(file_lines[0], "\t".join(params))

    def test_writes_metadata_to_existing_file(self):
        pass

    def test_interaction_is_logged_successful_infection(self):
        eboola = Virus("Eboola", 0.7, 0.9)
        random_already_sick_person = Person(6, False, eboola)
        random_unvax_person = Person(5, False)
        self.test_logger.log_interaction(
            random_already_sick_person, random_unvax_person, did_infect=True
        )
        last_line = self.temp_file.readlines()[-1]
        self.assertEqual(
            last_line,
            f"{random_already_sick_person._id} infects {random_unvax_person._id}",
        )

    def test_interaction_is_logged_unsuccessful_infection_because_of_vaccination(self):
        random_vax_person = Person(5, True)
        eboola = Virus("Eboola", 0.7, 0.9)
        random_already_sick_person = Person(6, False, eboola)
        self.test_logger.log_interaction(
            random_already_sick_person, random_vax_person, did_infect=False
        )
        last_line = self.temp_file.readlines()[-1]
        self.assertEqual(
            last_line,
            f"{random_already_sick_person._id} infects {random_vax_person._id}",
        )

    def test_interaction_is_logged_unsuccessful_infection_because_already_sick(self):
        eboola = Virus("Eboola", 0.7, 0.9)
        person1 = Person(4, False, eboola)
        random_already_sick_person = Person(6, False, eboola)
        self.test_logger.log_interaction(
            person1, random_already_sick_person, did_infect=False
        )
        last_line = self.temp_file.readlines()[-1]
        self.assertEqual(
            last_line, f"{person1._id} infects {random_already_sick_person._id}"
        )

    def test_infection_survival_is_logged(self):
        person2 = Person(7, True)
        self.test_logger.log_infection_survival(person2, False)
        last_line = self.temp_file.readlines()[-1]
        self.assertEqual(last_line, f"{person2._id} survived infection")

    def test_infection_survival_did_not_survive_is_logged(self):
        person2 = Person(7, True)
        self.test_logger.log_infection_survival(person2, False)
        last_line = self.temp_file.readlines()[-1]
        self.assertEqual(last_line, f"{person2._id} died from infection")

    def test_time_step(self):
        pass


if __name__ == "__main__":
    unittest.main()
