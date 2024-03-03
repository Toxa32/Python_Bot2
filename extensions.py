import requests
import json
from config import currencies


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_convert(curr_from, curr_to, amount):
        try:
            curr_from_key = currencies[curr_from]
        except KeyError:
            raise APIException(f'Валюта {curr_from} не найдена!\nСписок доступных валют см. /values')
        try:
            curr_to_key = currencies[curr_to]
        except KeyError:
            raise APIException(f'Валюта {curr_to} не найдена!\nСписок доступных валют см. /values')
        if curr_from_key == curr_to_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {curr_from}')
        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise APIException(f'Неудалось обработать количество: {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={curr_to_key}&tsyms={curr_from_key}&amount={amount}")
       
        result = json.loads(r.content)[currencies[curr_from_key]]
        return result
    