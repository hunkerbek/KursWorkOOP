from abc import ABC, abstractmethod


class abstract_vacancy_prov_class(ABC):
    @abstractmethod
    def get_vacancy(self, vacancy_name):
        pass

