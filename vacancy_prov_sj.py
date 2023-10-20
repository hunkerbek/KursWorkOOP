import os
from pprint import pprint

import requests

from abstractvacancyprovclass import AbstractVacancyProvClass
from vacancy import Vacancy


class VacancyProvSj(AbstractVacancyProvClass):
    API_KEY_SJ = os.getenv("API_KEY_SJ")
    def get_vacancy(self, vacancy_name):
        res = requests.get("https://api.superjob.ru/2.0/vacancies/",params={"keyword":vacancy_name},
                     headers={"X-Api-App-Id": self.API_KEY_SJ})
        if res.status_code==200:
            data=res.json()
            result = []
            #pprint(data)
            #return []
            for a in data["objects"]:
                salary_from = a.get("payment_from", None)
                salary_to = a.get("payment_to", None)

                new_vacancy=Vacancy(a["profession"],salary_from,salary_to,a["link"])
                result.append(new_vacancy)
            return result