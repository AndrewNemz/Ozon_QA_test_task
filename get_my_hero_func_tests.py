import unittest
import requests
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

    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_my_hero_unemployee_tallest(self, mock_get_heroes):
        """Тест на проверку самого высокого безработного героя"""
        mock_heroes_data = [
            {
                "name": "Test hero 1",
                "appearance": {"gender": "Female", "height": ["20", "190 cm"]},
                "work": {"occupation": "-"}
            },
            {
                "name": "Test hero 2",
                "appearance": {"gender": "Female", "height": ["10", "200 cm"]},
                "work": {"occupation": "Test work 2"}
            }
        ]
        mock_get_heroes.return_value = mock_heroes_data

        hero = Hero(gender='Female', is_employee=False)
        tallest_hero = hero.get_my_hero()

        self.assertEqual(tallest_hero["name"], "Test hero 1")

    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_my_hero_not_match_case(self, mock_get_heroes):
        """Тест на проверку несовпадающих условий."""
        mock_heroes_data = [
            {
                "name": "Test hero 1",
                "appearance": {"gender": "Female", "height": ["20", "190 cm"]},
                "work": {"occupation": "-"}
            },
            {
                "name": "Test hero 2",
                "appearance": {"gender": "Female", "height": ["10", "200 cm"]},
                "work": {"occupation": "-"}
            }
        ]
        mock_get_heroes.return_value = mock_heroes_data

        hero_not_match_is_employee = Hero(gender='Female', is_employee=True)
        hero_not_match_gender = Hero(gender='Male', is_employee=False)

        tallest_hero_is_employee = hero_not_match_is_employee.get_my_hero()
        tallest_hero_gender = hero_not_match_gender.get_my_hero()

        self.assertEqual(tallest_hero_is_employee, None)
        self.assertEqual(tallest_hero_gender, None)

    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_my_hero_gender_is_none(self, mock_get_heroes):
        """Тест на проверку незаданного пола."""
        mock_heroes_data = [
            {
                "name": "Test hero 1",
                "appearance": {"gender": "Female", "height": ["20", "190 cm"]},
                "work": {"occupation": "-"}
            },
            {
                "name": "Test hero 2",
                "appearance": {"gender": "Male", "height": ["10", "200 cm"]},
                "work": {"occupation": "-"}
            }
        ]
        mock_get_heroes.return_value = mock_heroes_data

        hero_is_employee = Hero(gender=None, is_employee=True)
        hero_is_unemployee = Hero(gender=None, is_employee=False)

        tallest_hero_is_employee = hero_is_employee.get_my_hero()
        tallest_hero_hero_is_unemployee = hero_is_unemployee.get_my_hero()

        self.assertEqual(tallest_hero_is_employee, None)
        self.assertEqual(tallest_hero_hero_is_unemployee, None)

    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_my_hero_height_is_none(self, mock_get_heroes):
        """Тест на проверку случая, когда height - None."""
        mock_heroes_data = [
            {
                "name": "Test hero 1",
                "appearance": {"gender": "Female", "height": None},
                "work": {"occupation": "Test work 1"}
            },
            {
                "name": "Test hero 2",
                "appearance": {"gender": "Male", "height": None},
                "work": {"occupation": "-"}
            }
        ]
        mock_get_heroes.return_value = mock_heroes_data

        hero_is_employee = Hero(gender='Female', is_employee=True)
        hero_is_unemployee = Hero(gender='Male', is_employee=False)

        tallest_hero_is_employee = hero_is_employee.get_my_hero()
        tallest_hero_hero_is_unemployee = hero_is_unemployee.get_my_hero()

        self.assertEqual(tallest_hero_is_employee, None)
        self.assertEqual(tallest_hero_hero_is_unemployee, None)

    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_my_hero_unnormal_gender_register(self, mock_get_heroes):
        """Тест на проверку случая, когда gender задан некорректным регистром."""
        mock_heroes_data = [
            {
                "name": "Test hero 1",
                "appearance": {"gender": "Female", "height": ["20", "190 cm"]},
                "work": {"occupation": "Test work 1"}
            },
            {
                "name": "Test hero 2",
                "appearance": {"gender": "Male", "height": ["20", "190 cm"]},
                "work": {"occupation": "-"}
            }
        ]
        mock_get_heroes.return_value = mock_heroes_data

        hero_is_employee = Hero(gender='fEMaLe', is_employee=True)
        hero_is_unemployee = Hero(gender='mAlE', is_employee=False)

        tallest_hero_is_employee = hero_is_employee.get_my_hero()
        tallest_hero_hero_is_unemployee = hero_is_unemployee.get_my_hero()

        self.assertEqual(tallest_hero_is_employee['name'], "Test hero 1")
        self.assertEqual(tallest_hero_hero_is_unemployee['name'], "Test hero 2")
    
    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_my_hero_empty_list(self, mock_get_heroes):
        """Тест на проверку пустого списка героев."""
        mock_heroes_data = []
        mock_get_heroes.return_value = mock_heroes_data

        hero = Hero(gender='Female', is_employee=False)
        tallest_hero = hero.get_my_hero()

        self.assertEqual(tallest_hero, None)

    def test_get_data_success(self):
        """Успешный HTTP ответ 200 с реальной конечной точкой API."""
        hero = Hero('Male', True)

        data = hero.get_heroes()
        response = requests.get(hero._url)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)

    def test_get_data_bad_request(self):
        """HTTP ответ 404 с конечной точкой API."""
        hero = Hero('Female', True, 'https://akabab.github.io/superhero-api/api/not_found')

        data = hero.get_heroes()
        response = requests.get(hero._url)

        self.assertEqual(response.status_code, 404)
        self.assertIsNone(data)

    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_heroes_400(self, mock_get_heroes):
        """HTTP ответ 400 с моковой конечной точкой API."""

        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "Bad Request", response=mock_response
        )
        mock_response.json.return_value = {"error": "Invalid input"}

        mock_get_heroes.return_value = None

        hero = Hero('Female', True)
        data = hero.get_heroes()

        self.assertIsNone(data)

    @patch('test_superhero_api.Hero.get_heroes')
    def test_get_heroes_500(self, mock_get_heroes):
        """HTTP ответ 500 с моковой конечной точкой API."""

        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "Internal Server Error", response=mock_response
        )
        mock_response.json.return_value = {"error": "Something went wrong on the server."}

        mock_get_heroes.return_value = None

        hero = Hero('Female', True)
        data = hero.get_heroes()

        self.assertIsNone(data)
