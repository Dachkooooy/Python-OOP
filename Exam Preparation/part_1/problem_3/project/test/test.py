from project.senior_student import SeniorStudent
from unittest import TestCase, main

class SeniorStudentTests(TestCase):
    student_id = "0123"
    name = "Test"
    student_gpa = 4.5

    def setUp(self):
        self.senior_student = SeniorStudent(self.student_id, self.name, self.student_gpa)

    def test_init(self):
        self.assertEqual(self.student_id, self.senior_student.student_id)
        self.assertEqual(self.name, self.senior_student.name)
        self.assertEqual(self.student_gpa, self.senior_student.student_gpa)
        self.assertEqual(len(self.senior_student.colleges), 0)
        self.assertIsInstance(self.senior_student.colleges, set)

    def test_student_id_too_short(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!",  str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_id = " 123 "
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_student_id_with_spaces_strip(self):
        self.senior_student.student_id = " 1234 "
        self.assertEqual("1234", self.senior_student.student_id)

    def test_student_name_valid(self):
        self.senior_student.name = "John Dow"
        self.assertEqual("John Dow", self.senior_student.name)

    def test_student_name_empty(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.senior_student.name = "   "
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_student_gpa_valid(self):
        self.senior_student.student_gpa = 4.5
        self.assertEqual(4.5, self.senior_student.student_gpa)

    def test_student_gpa_invalid_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_gpa = 0.8
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_applying_to_college_with_low_student_gpa(self):
        expected = 'Application failed!'
        actual = self.senior_student.apply_to_college(4.6, "Yale")
        self.assertEqual(expected, actual)
        self.assertEqual(0, len(self.senior_student.colleges))

    def test_applying_to_college_with_high_student_gpa(self):
        expected = 'Test successfully applied to Yale.'
        actual = self.senior_student.apply_to_college(4.0, "Yale")
        self.assertEqual(expected, actual)
        self.assertEqual(1, len(self.senior_student.colleges))
        self.assertIn("YALE", self.senior_student.colleges)

    def test_applying_to_same_college_multiple_times(self):
        self.senior_student.apply_to_college(4.1, "Yale")
        self.senior_student.apply_to_college(4.1, "Yale")
        self.assertEqual(1, len(self.senior_student.colleges))

    def test_update_gpa_unsuccessfully(self):
        expected = "The GPA has not been changed!"
        actual = self.senior_student.update_gpa(1.0)
        self.assertEqual(expected, actual)
        self.assertEqual(4.5, self.senior_student.student_gpa)

        expected = "The GPA has not been changed!"
        actual = self.senior_student.update_gpa(0.7)
        self.assertEqual(expected, actual)
        self.assertEqual(4.5, self.senior_student.student_gpa)

    def test_update_gpa_successfully(self):
        expected = 'Student GPA was successfully updated.'
        actual = self.senior_student.update_gpa(3.0)
        self.assertEqual(expected, actual)
        self.assertEqual(3.0, self.senior_student.student_gpa)

    def test__eq__equal(self):
        another_senior_student = SeniorStudent("5555", "Test2", 4.5)
        self.assertTrue(self.senior_student == another_senior_student)

    def test__eq__not_equal(self):
        another_senior_student = SeniorStudent("5555", "Test2", 4.0)
        self.assertFalse(self.senior_student == another_senior_student)

        another_senior_student = SeniorStudent("5555", "Test2", 5)
        self.assertFalse(self.senior_student == another_senior_student)

if __name__ == "__main__":
    main()