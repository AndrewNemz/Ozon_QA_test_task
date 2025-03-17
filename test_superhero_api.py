import structlog
import requests

logger = structlog.getLogger(__name__)


class Hero:
    def __init__(
            self,
            gender: str,
            is_employee: bool,
            url: str = 'https://akabab.github.io/superhero-api/api/all.json'
    ):
        self._gender = gender
        self._is_employee = is_employee
        self._url = url

    def get_heroes(self):
        try:
            logger.info(
                'Метод get_heroes получает героев по url: ', url=self._url
            )
            response = requests.get(self._url)
            response.raise_for_status()
            data = response.json()
            return data
        # TODO можно написат эксепшн HTTPError
        except Exception as e:
            logger.error('Неизвестная ошибка: %s', e)
            raise e

    def is_employed(self, hero):
        try:
            work = hero.get('work', {})
            if not self._is_employee:
                if work['occupation'] == '-':
                    return True
                else:
                    return False
            else:
                if work['occupation'] != '-':
                    return True
                else:
                    return False
        except Exception as e:
            logger.error('Неизвестная ошибка: %s', e)
            raise e

    def get_height(self, hero):
        try:
            height = hero.get('appearance').get('height')[1]
            if height is None:
                return None
            return float(height.split()[0])
        except Exception as e:
            logger.error('Неизвестная ошибка: %s', e)
            raise e

    def get_tallest_hero(self, selected_heroes):
        try:
            if not selected_heroes:
                logger.info('Список героев пуст')
                return

            talles_hero = None
            max_height = 0

            for hero in selected_heroes:
                height = self.get_height(hero)
                if height >= max_height:
                    max_height = height
                    talles_hero = hero

            return talles_hero
        except Exception as e:
            logger.error('Неизвестная ошибка: %s', e)
            raise e

    def get_my_hero(self) -> dict:
        try:
            logger.info(
                'Метод get_my_hero: ',
                gender=self._gender, is_work=self._is_employee
            )
            heroes_data = self.get_heroes()
            selected_heroes = [
                hero for hero in heroes_data if hero.get(
                    'appearance'
                ).get('gender') == self._gender and self.is_employed(hero)
            ]
            return self.get_tallest_hero(selected_heroes)
        except Exception as e:
            logger.error('Неизвестная ошибка: %s', e)
            raise e

# hero_1 = Hero('Male', False)
# print(hero_1.get_my_hero())