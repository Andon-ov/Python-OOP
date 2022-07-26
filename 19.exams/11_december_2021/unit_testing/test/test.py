from unittest import TestCase, main

from project.team import Team


class TeamTest(TestCase):
    def setUp(self) -> None:
        name = 'MyTeam'
        name2 = 'OtherTeam'

        self.team_test = Team(name)
        self.other_team_test = Team(name2)

    def test_team_init(self):
        expected_result = 'MyTeam'
        actual_result = self.team_test.name

        self.assertEqual(expected_result, actual_result)
        self.assertEqual({}, self.team_test.members)

    def test_property_name(self):
        expected_result = 'MyTeam'
        actual_result = self.team_test.name

        self.assertEqual(expected_result, actual_result)

    def test_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.team_test.name = 'My Team'
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_work_correctly(self):
        actual_result = self.team_test.add_member(Kolio=20, Pesho=22)
        expected_result = "Successfully added: Kolio, Pesho"

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.team_test.members, {'Kolio': 20, 'Pesho': 22})

    def test_remove_member_work_correctly(self):
        self.team_test.add_member(Kolio=20, Pesho=22)
        actual_result = self.team_test.remove_member('Kolio')
        expected_result = "Member Kolio removed"

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.team_test.members, {'Pesho': 22})

    def test_remove_member_does_not_exist(self):
        self.team_test.add_member(Kolio=20, Pesho=22)
        actual_result = self.team_test.remove_member('Joro')
        expected_result = f"Member with name Joro does not exist"

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.team_test.members, {'Kolio': 20, 'Pesho': 22})

    def test__gt__if_false(self):
        result = self.team_test.__gt__(self.other_team_test)
        self.assertFalse(result)

    def test__gt__if_true(self):
        self.team_test.add_member(Kolio=20, Pesho=22)
        result = self.team_test.__gt__(self.other_team_test)
        self.assertTrue(result)

    def test___len__(self):
        self.team_test.add_member(Kolio=20, Pesho=22)
        expected_result = 2
        actual_result = self.team_test.__len__()

        self.assertEqual(actual_result, expected_result)

    def test___add__(self):
        self.team_test.add_member(Kolio=20, Pesho=22)
        self.other_team_test.add_member(Joro=20, Valio=22)

        last_team = self.team_test.__add__(self.other_team_test)
        expected_result = f"{self.team_test.name}{self.other_team_test.name}"
        actual_result = last_team.name
        self.assertEqual(expected_result, actual_result)
        all_members = {'Joro': 20, 'Kolio': 20, 'Pesho': 22, 'Valio': 22}
        self.assertEqual(last_team.members, all_members)

    def test___str__(self):
        self.team_test.add_member(Kolio=20, Pesho=22)
        actual_result = str(self.team_test)
        expected_result = 'Team name: MyTeam\nMember: Pesho - 22-years old\nMember: Kolio - 20-years old'
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    main()
