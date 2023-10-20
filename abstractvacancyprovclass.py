from abc import ABC, abstractmethod


class AbstractVacancyProvClass(ABC):
    """Абстракный класс поставщик вакансий"""

    @abstractmethod
    def get_vacancy(self, vacancy_name:str):
        """Получить список вакансий по строке запроса"""
        pass

