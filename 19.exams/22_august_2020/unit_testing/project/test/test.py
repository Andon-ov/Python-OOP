from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class StudentReportCardTest(TestCase):
    def setUp(self) -> None:
        self.student_name: str = 'Kolio'
        self.school_year: int = 11

        self.test_student = StudentReportCard(self.student_name, self.school_year)

    def test_student_report_card_init(self):
        self.assertEqual(self.test_student.student_name, self.student_name)
        self.assertEqual(self.test_student.school_year, self.school_year)
        self.assertEqual(self.test_student.grades_by_subject, {})

    # def test_student_name_setter_work_currently(self):
    #     new_student_name = 'Ivan'
    #
    #     self.test_student.student_name = new_student_name
    #     result = self.test_student.student_name
    #     self.assertEqual(result, new_student_name)

    def test_student_name__raise_value_error_student__name_cannot_be_empty_string(self):
        new_student_name = ''
        with self.assertRaises(ValueError) as ex:
            self.test_student.student_name = new_student_name
        self.assertEqual(str(ex.exception), "Student Name cannot be an empty string!")

    # def test__school_year_setter__work_currently(self):
    #     actual_result = self.test_student.school_year = 10
    #     expected_result = self.test_student.school_year
    #     self.assertEqual(actual_result, expected_result)

    def test_student_name__raise_value_error__year_must_be_between_1_and_12(self):
        new_school_year = 13
        with self.assertRaises(ValueError) as ex:
            self.test_student.school_year = new_school_year
        self.assertEqual(str(ex.exception), "School Year must be between 1 and 12!")

    # def test_add_grade_work_currently(self):
    #     grade = 4
    #     self.test_student.add_grade(self.student_name, grade)
    #     other_test_student = 'Joro'
    #     self.test_student.add_grade(other_test_student, grade)
    #
    #     self.assertIn(self.student_name, self.test_student.grades_by_subject)
    #     self.assertIn(grade, self.test_student.grades_by_subject[self.student_name])
    #
    #     actual_result = self.test_student.grades_by_subject
    #     expected_result = {'Joro': [4], 'Kolio': [4]}
    #     self.assertEqual(actual_result, expected_result)

    # def test_add_grade_if_obj_already_in(self):
    #     grade = 6
    #     self.test_student.add_grade(self.student_name, grade)
    #
    #     self.test_student.add_grade(self.student_name, grade)
    #     actual_result = self.test_student.grades_by_subject
    #     expected_result = {self.student_name: [grade, grade]}
    #     self.assertEqual(actual_result, expected_result)

    def test_average_grade_by_subject(self):
        grade = 6
        other_grade = 4
        other_test_student = 'Joro'
        for _ in range(3):
            self.test_student.add_grade(self.student_name, grade)

            self.test_student.add_grade(other_test_student, other_grade)

        actual_result = self.test_student.grades_by_subject
        expected_result = {'Joro': [4, 4, 4], 'Kolio': [6, 6, 6]}
        self.assertEqual(actual_result, expected_result)

        # self.assertEqual(len(self.test_student.grades_by_subject[self.test_student.student_name]), 3)
        # self.assertEqual(len(self.test_student.grades_by_subject[other_test_student]), 3)

        self.assertEqual(self.test_student.average_grade_by_subject(), 'Kolio: 6.00\nJoro: 4.00')

    def test_average_grade_for_all_subjects(self):
        grade = 6
        other_grade = 4
        other_test_student = 'Joro'

        self.test_student.add_grade(self.student_name, grade)
        self.test_student.add_grade(self.student_name, grade)
        self.test_student.add_grade(self.student_name, grade)
        self.test_student.add_grade(other_test_student, other_grade)
        self.test_student.add_grade(other_test_student, other_grade)
        self.test_student.add_grade(other_test_student, grade)

        actual_result = self.test_student.average_grade_for_all_subjects()
        expected_result = 'Average Grade: 5.33'

        self.assertEqual(actual_result, expected_result)

    def test_repr_work_currently(self):
        grade = 6
        other_grade = 4
        other_test_student = 'Joro'

        self.test_student.add_grade(self.student_name, grade)
        self.test_student.add_grade(self.student_name, grade)
        self.test_student.add_grade(self.student_name, grade)
        self.test_student.add_grade(other_test_student, other_grade)
        self.test_student.add_grade(other_test_student, other_grade)
        self.test_student.add_grade(other_test_student, grade)

        actual_result = repr(self.test_student)
        result = f"Name: {self.student_name}\nYear: {self.school_year}\n----------\n{self.test_student.average_grade_by_subject()}\n----------\n{self.test_student.average_grade_for_all_subjects()}"
        self.assertEqual(actual_result, result)


if __name__ == '__main__':
    main()
