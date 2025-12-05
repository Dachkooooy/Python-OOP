from unittest import TestCase, main
from project.hero import Hero

class HeroTests(TestCase):
    username = "Test hero"
    level = 5
    health  = 16.8
    damage = 9.4

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_class_attributes_types_valid(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_equal_hero_username_to_enemy_username_raises(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_zero_and_less_health_raises(self):
        self.hero.health = 0
        enemy = Hero("Test enemy", self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health = -1
        enemy = Hero("Test enemy", self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex2:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex2.exception))

    def test_enemy_zero_and_less_health_raises(self):
        enemy = Hero("Test enemy", self.level, 0, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Test enemy. He needs to rest", str(ex.exception))

        enemy = Hero("Test enemy", self.level, -1, self.damage)
        with self.assertRaises(Exception) as ex2:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Test enemy. He needs to rest", str(ex2.exception))

    def test_draw_health_hero_and_enemy(self):
        enemy = Hero("Test enemy", self.level, self.health, self.damage)
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-30.2, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_wins(self):
        enemy = Hero("Test enemy", 1, 1, 1)
        result = self.hero.battle(enemy)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(20.8, self.hero.health)
        self.assertEqual(14.4, self.hero.damage)
        self.assertEqual("You win", result)

    def test_hero_loses(self):
        self.hero.health = 10
        self.hero.damage = 10
        enemy = Hero("Test enemy", 100, 100, 100)
        result = self.hero.battle(enemy)

        self.assertEqual(101, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(105, enemy.damage)
        self.assertEqual("You lose", result)

    def test_str(self):
        expected_value = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(expected_value, self.hero.__str__())


if __name__ == '__main__':
    main()