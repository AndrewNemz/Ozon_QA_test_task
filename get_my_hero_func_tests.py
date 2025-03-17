import unittest
from unittest.mock import patch, Mock

from test_superhero_api import Hero


class TestHero(unittest.TestCase):
    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_my_hero_male_tallest(self, mock_get_heroes):
        """Тест на проверку самого высокого героя мужчины."""
        mock_heroes_data = [
            {
                "name": "Test hero 1",
                "appearance": {"gender": "Male", "height": ["20", "190 cm"]},
                "work": {"occupation": "Test work 1"}
            },
            {
                "name": "Test hero 2",
                "appearance": {"gender": "Male", "height": ["10", "180 cm"]},
                "work": {"occupation": "Test work 2"}
            }
        ]
        mock_get_heroes.return_value = mock_heroes_data

        hero = Hero(gender='Male', is_employee=True)
        tallest_hero = hero.get_my_hero()

        self.assertEqual(tallest_hero["name"], "Test hero 1")

    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_my_hero_female_tallest(self, mock_get_heroes):
        """Тест на проверку самого высокого героя женщины"""
        mock_heroes_data = [
            {
                "name": "Test hero 1",
                "appearance": {"gender": "Female", "height": ["20", "190 cm"]},
                "work": {"occupation": "Test work 1"}
            },
            {
                "name": "Test hero 2",
                "appearance": {"gender": "Female", "height": ["10", "200 cm"]},
                "work": {"occupation": "Test work 2"}
            }
        ]
        mock_get_heroes.return_value = mock_heroes_data

        hero = Hero(gender='Female', is_employee=True)
        tallest_hero = hero.get_my_hero()

        self.assertEqual(tallest_hero["name"], "Test hero 2")


        #TODO ошибки http, пустой список героев, один безработный мж
