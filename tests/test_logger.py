import os
import unittest

from logger import Logger

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.temp_file_name = 'temp_logs.txt'
        self.temp = open(self.temp_file_name, 'w+')
        self.test_logger = Logger(self.temp_file_name)

    def tearDown(self):
        os.remove('temp_logs.txt')

    def test_logger_initialization(self):
        self.assertEqual(self.test_logger.file_name, self.temp_file_name)

    def test_writes_metadata_to_new_file(self):
        file_lines = self.temp.readlines()
        self.assertEqual(len(file_lines), 0)

        params = [100, .5, "big v", .9, 10]
        self.test_logger.write_metadata(*params)
        self.assertEqual(file_lines[0], '\t'.join(params))

    def test_writes_metadata_to_existing_file(self):
        pass

    def test_interaction_is_logged(self):
        pass

    def test_infection_survival_is_logged(self):
        pass

    def test_time_step(self):
        pass

if __name__ == "__main__":
    unittest.main()
