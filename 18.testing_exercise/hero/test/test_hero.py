from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self):
        # username: str, level: int, health: float, damage: float
        self.test_hero = Hero("Donko", 99, 99.99, 99.99)
        self.test_enemy = Hero("Kiro", 99, 99.99, 99.99)

    def test_hero_init(self):
        self.assertEqual("Donko", self.test_hero.username)
        self.assertEqual(99, self.test_hero.level)
        self.assertEqual(99.99, self.test_hero.health)
        self.assertEqual(99.99, self.test_hero.damage)

    def test_battle_raise_exception_cannot_fight_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(self.test_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raise_value_error_your_health_is_lower(self):
        self.test_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(self.test_enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.test_hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(self.test_enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_raise_value_error_enemy_health_is_lower(self):
        self.test_enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(self.test_enemy)
        self.assertEqual(f"You cannot fight {self.test_enemy.username}. He needs to rest", str(ex.exception))

        self.test_enemy.health = -1
        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(self.test_enemy)
        self.assertEqual(f"You cannot fight {self.test_enemy.username}. He needs to rest", str(ex.exception))

    def test_str_is_correct(self):
        actual_result = self.test_hero.__str__()
        expected_result = f"Hero {self.test_hero.username}: {self.test_hero.level} lvl\n" \
                          f"Health: {self.test_hero.health}\n" \
                          f"Damage: {self.test_hero.damage}\n"
        self.assertEqual(actual_result, expected_result)

    def test_battle_returns_draw_when_both_heroes_die(self):
        result = self.test_hero.battle(self.test_enemy)
        self.assertEqual(result, "Draw")
        self.assertEqual(-9799.02, self.test_hero.health)
        self.assertEqual(-9799.02, self.test_enemy.health)

    def test_hero_win(self):
        self.test_enemy.damage = 1
        self.test_enemy.level = 1
        self.test_enemy.health = 1

        result = self.test_hero.battle(self.test_enemy)
        self.assertEqual("You win", result)
        self.assertEqual(100, self.test_hero.level)
        self.assertEqual(103.99, self.test_hero.health)
        self.assertEqual(104.99, self.test_hero.damage)

    def test_hero_lost(self):
        self.test_hero.damage = 1
        self.test_hero.level = 1
        self.test_hero.health = 1

        result = self.test_hero.battle(self.test_enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(100, self.test_enemy.level)
        self.assertEqual(103.99, self.test_enemy.health)
        self.assertEqual(104.99, self.test_enemy.damage)


if __name__ == "__main__":
    main()
