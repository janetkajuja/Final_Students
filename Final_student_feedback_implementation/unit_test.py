"""This is unit test for the student project"""
import unittest
import final_assignment_module as testing

TEST_DATA = testing.StudentsId()
TEST_VALID_PASSWORD = testing.is_valid_password(password="Password123@#")
TEST_INVALID_PASSWORD = testing.is_valid_password(password="Password123@=+!")
TEST_UPDATE = testing.StudentsInfo()
TEST_FILE = testing.FileFormat()

FILE = "students.txt"
FINAL_FILE = "final_students.txt"


class TestCase(unittest.TestCase):
    """This is all testcases for the students project"""

    def test_file(self):
        """This is a testcase for loading a file student"""
        valid_file = TEST_DATA.load_students()
        self.assertEqual(valid_file,
                         {'001': 'id:001,firstname:Eric,lastname:Smith,password:dfghjDFGHJ123#',
                          '002': 'id:002,firstname:Alice,lastname:Brown,password:DFGHdfghj123#',
                          '003': 'id:003,firstname:Robert,lastname:Rock,password:DFGHJdfghj123#'})

    def test_valid_id(self):
        """This is a testcase for checking valid ID's"""
        id_part = TEST_DATA.is_valid_id("001")
        self.assertTrue(id_part)

    def test_invalid_id(self):
        """This is a testcase for checking invalid ID's"""
        id_part = TEST_DATA.is_valid_id("0 0 1")
        self.assertFalse(id_part)

    def test_valid_password(self):
        """This is a testcase for checking a valid password"""
        valid_pass = TEST_VALID_PASSWORD
        self.assertTrue(valid_pass)

    def test_invalid_password(self):
        """This is a testcase for checking invalid password"""
        invalid_pass = TEST_INVALID_PASSWORD
        self.assertFalse(invalid_pass)

    def test_update(self):
        """This is a testcase for checked if record is updated"""
        update = TEST_UPDATE.is_record_updated(FINAL_FILE, "001")
        self.assertTrue(update)

    def test_invalid_record(self):
        """This is a testcase for checking if invalid ID can be updated"""
        invalid_record = TEST_UPDATE.is_record_updated(FINAL_FILE, "0 0 1")
        self.assertFalse(invalid_record)


if __name__ == "__main__":
    unittest.main()
