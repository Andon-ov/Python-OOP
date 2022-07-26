from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):

    def setUp(self) -> None:
        name = 'BaiDo'
        courses = {
            'OOP': ["BaiDo note"]
        }

        self.test_student = Student(name, courses)

    def test_student_init(self):
        name = 'BaiDo'
        only_name_test = Student(name)

        expected_result = name
        actual_result = only_name_test.name

        self.assertEqual(actual_result, expected_result)
        self.assertEqual({}, only_name_test.courses)

    def test_student_init_with_courses(self):
        name = 'BaiDo'
        courses = {
            'OOP': ["BaiDo note"]
        }
        expected_result = name
        actual_result = self.test_student.name
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(courses, self.test_student.courses)

    def test_enroll_course_already_added(self):
        course = 'OOP'
        expected_result = "Course already added. Notes have been updated."
        actual_result = self.test_student.enroll("OOP", ["note3"])

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(['BaiDo note', 'note3'], self.test_student.courses[course])

    def test_enroll_course_and_course_notes_have_been_added_with_y(self):
        course = "Django"
        notes = ["note4", "note5"]
        expected_result = "Course and course notes have been added."
        actual_result = self.test_student.enroll(course, notes, 'Y')

        self.assertEqual(actual_result, expected_result)
        self.assertTrue(course in self.test_student.courses)
        self.assertEqual(notes, self.test_student.courses[course])

    def test_enroll_course_and_course_notes_have_been_added_with_empty_string(self):
        course = "Django"
        notes = ["note4", "note5"]
        expected_result = "Course and course notes have been added."
        actual_result = self.test_student.enroll(course, notes, '')

        self.assertEqual(actual_result, expected_result)
        self.assertTrue(course in self.test_student.courses)
        self.assertEqual(notes, self.test_student.courses[course])

    def test_enroll_course_have_been_added(self):
        course = "Django"
        notes = ["note4", "note5"]

        expected_result = "Course has been added."
        actual_result = self.test_student.enroll(course, notes, 'N')

        self.assertEqual(actual_result, expected_result)
        self.assertTrue(course in self.test_student.courses)
        self.assertEqual([], self.test_student.courses[course])

    def test_add_notes_notes_have_been_updated(self):
        course = "OOP"
        notes = "note10"

        expected_result = "Notes have been updated"
        actual_result = self.test_student.add_notes(course, notes)
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(['BaiDo note', 'note10'], self.test_student.courses[course])

    def test_add_notes_raise_exception_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.test_student.add_notes("OPP", "The Note")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_course_has_been_removed(self):
        course = "Django"
        notes = ["note4", "note5"]
        self.test_student.enroll(course, notes, '')

        expected_result = "Course has been removed"
        actual_result = self.test_student.leave_course("OOP")

        self.assertEqual(actual_result, expected_result)
        self.assertEqual({'Django': ['note4', 'note5']}, self.test_student.courses)

    def test_leave_course_raise_exception_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course("OPP", )
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
