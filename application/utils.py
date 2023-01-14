from typing import NamedTuple, List

import requests

NUM_OF_VACANCIES = 10

class Data(NamedTuple):
    name: str
    misc: List[str]


def get_vacancies(vac_name):
    data = []
    r = requests.get(f'https://api.hh.ru/vacancies/?text={vac_name}')
    result = r.json()
    vacancies = result.get('items', [])
    if len(vacancies) > NUM_OF_VACANCIES:
        vacancies = vacancies[:NUM_OF_VACANCIES]
    for vac in vacancies:
        r = requests.get(f'https://api.hh.ru/vacancies/{vac.get("id")}')
        result = dict(r.json())
        data.append(
            Data(
                name=result.get('name'),
                misc=[result.get('description'), 
                      ", ".join([i.get('name') for i in result.get('key_skills')]), 
                      result.get('employer', {}).get('name'), 
                      result['salary']['from'] if result.get('salary') else '', 
                      result.get('area', {}).get('name'), result.get('published_at').split('T')[0]
                      ]
            )
        )
    return data
