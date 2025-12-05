from unittest import TestCase, main
from project.student import Student

class StudentTests(TestCase):

    def setUp(self):
        self.first_student = Student("Student 1 test", {"Python": ["note1", "note2"], "JS": ["note3"]})
        self.second_student = Student("Student 2 test")

    def test_init_with_courses(self):
        self.assertEqual("Student 1 test", self.first_student.name)
        self.assertEqual({"Python": ["note1", "note2"], "JS": ["note3"]}, self.first_student.courses)
        self.assertIsInstance(self.first_student.name, str)
        self.assertIsInstance(self.first_student.courses, dict)

    def test_init_without_courses(self):
        self.assertEqual("Student 2 test", self.second_student.name)
        self.assertEqual({}, self.second_student.courses)
        self.assertIsInstance(self.second_student.name, str)
        self.assertIsInstance(self.first_student.courses, dict)

    def test_enroll_in_existing_course(self):
        result = self.first_student.enroll("Python", ["note4", "note5"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["note1", "note2", "note4", "note5"], "JS": ["note3"]}, self.first_student.courses)

    def test_enroll_in_nonexisting_course_adding_notes_with_y(self):
        result = self.first_student.enroll("C#", ["note4", "note5"], "Y")
        self.assertIn("C#", self.first_student.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note4", "note5"], self.first_student.courses["C#"])

    def test_enroll_in_nonexisting_course_adding_notes_with_empty_str(self):
        result = self.first_student.enroll("C#", ["note4", "note5"], "")
        self.assertIn("C#", self.first_student.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note4", "note5"], self.first_student.courses["C#"])

    def test_enroll_in_nonexisting_course_not_adding_notes(self):
        result = self.second_student.enroll("C#", ["note4", "note5"], "N")
        self.assertIn("C#", self.second_student.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.second_student.courses["C#"])

    def test_add_notes_to_existing_course(self):
        self.second_student.enroll("C#", ["note4", "note5"], "Y")
        result = self.second_student.add_notes("C#", "note6")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note4", "note5", "note6"], self.second_student.courses["C#"])

    def test_add_notes_to_nonexisting_course(self):
        with self.assertRaises(Exception) as ex:
            self.second_student.add_notes("C#", "note1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.first_student.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.first_student.courses)

    def test_leave_nonexisting_course(self):
        with self.assertRaises(Exception) as ex:
            self.first_student.leave_course("C#")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()