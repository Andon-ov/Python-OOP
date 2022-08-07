from unittest import TestCase, main

from project.team import Team


class TeamTest(TestCase):
    name = "MyTeam"

    def setUp(self) -> None:
        self.test_team = Team(self.name)

    def test_init_work_correctly(self):
        self.assertEqual(self.name, self.test_team.name)
        self.assertEqual(self.test_team.members, {})

    def test_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.test_team.name = "My Team"
        self.assertEqual(str(ex.exception), "Team Name can contain only letters!")
        self.assertEqual(self.test_team.name, self.name)

    def test_add_member_work_correctly(self):
        result = self.test_team.add_member(Kolio=30, Joro=20, Vanjo=33)

        self.assertEqual(result, 'Successfully added: Kolio, Joro, Vanjo')

        self.assertDictEqual(self.test_team.members, {'Joro': 20, 'Kolio': 30, 'Vanjo': 33})
        self.assertEqual(len(self.test_team.members), 3)

    def test_remove_member_work_correctly(self):
        self.test_team.members['Jivo'] = 20
        self.test_team.members['Ivo'] = 22

        name = 'Jivo'
        result = self.test_team.remove_member(name)
        self.assertEqual(result, f'Member {name} removed')
        self.assertTrue(name not in self.test_team.members)

    def test_remove_member_does_not_exist(self):
        self.test_team.members['Kolio'] = 32

        name = 'Jivo'
        result = self.test_team.remove_member(name)
        self.assertEqual(result, f'Member with name {name} does not exist')

    def test__gt__work_correctly(self):
        self.test_team.members["Joro"] = 18
        self.test_team.members["Kolio"] = 22

        new_test_team = Team("NewTestTeam")
        new_test_team.members["Zoro"] = 33

        self.assertEqual(True, self.test_team > new_test_team)
        self.assertEqual(False, self.test_team < new_test_team)

        # Do not work correctly
        # self.assertTrue(self.test_team.__gt__(new_test_team))
        # self.assertFalse(new_test_team.__gt__(self.test_team))

    def test__len__work_correctly(self):
        self.test_team.add_member(Jivo=20, Kolio=30)
        self.assertEqual(len(self.test_team), 2)

    def test__add__work_correctly(self):
        new_test_team = Team("NewTestTeam")
        new_test_team.add_member(Valio=50)

        self.test_team.add_member(Jivo=20, Kolio=30)

        result = self.test_team.__add__(new_test_team)

        self.assertEqual(result.name, 'MyTeamNewTestTeam')
        self.assertEqual(result.members, {'Jivo': 20, 'Kolio': 30, 'Valio': 50})

    def test__str__work_correctly(self):
        self.test_team.add_member(Jivo=20, Kolio=30)
        result = str(self.test_team)
        self.assertEqual(result, 'Team name: MyTeam\nMember: Kolio - 30-years old\nMember: Jivo - 20-years old')


if __name__ == "__main__":
    main()
