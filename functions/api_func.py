from aiohttp import ClientSession
from pycbrf import ExchangeRates
# import aiofiles

# from pprint import pp

from functions.config_reader import config


api_weather = config.api_weather
api_crypto = config.api_crypto


# Api погоды
async def get_city_world(city, country_code: str) -> str:
    async with ClientSession() as session:
        base_url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': [city, country_code], 'appid': api_weather, 'units': 'metric'}
        async with session.get(url=base_url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return data['main']['temp']
            else:
                return False


# Api криптовалюты
async def get_cryptocurrency_rate(id: int) -> int:
    headers = {'X-Api-Key': api_crypto}

    async with ClientSession(headers=headers) as session:
        base_url = f'https://api.cryptorank.io/v2/currencies/{id}'
        async with session.get(url=base_url) as response:
            data: dict = await response.json()
            price: dict = data['data']['price']
            return price
            # path_file = r'D:\Project\GetApi_bot\functions\output.txt'
            # async with aiofiles.open(file=path_file, mode='a', encoding='utf-8') as file:
            #     for k in d:
            #         await file.write(f'{k['id']}-{k['key']} \n')
                # pp(k['id'])
                # pp(k['key'])


# Курсы валют
def get_currency_rate(rate: str) -> int:
    rates = ExchangeRates()
    usd_rate = rates[rate].value
    return int(usd_rate)
