import aiohttp
from pycbrf import ExchangeRates
from os import getenv
from dotenv import load_dotenv


load_dotenv()
api_weather = getenv('api_weather')
api_crypto = getenv('api_crypto')


# Api погоды
async def get_city_world(city, country_code: str) -> str:
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_weather}&units=metric'
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url) as response:
            if response.status == 200:
                data = await response.json()
                return data['main']['temp']
            else:
                return False


# Api криптовалюты
async def get_cryptocurrency_rate(id: int) -> int:
    base_url = f'https://api.cryptorank.io/v1/currencies?api_key={api_crypto}'
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url) as response:
            data = await response.json()
            price = data['data'][id]['values']['USD']['price']
            return int(price)


# Курсы валют
def get_currency_rate(rate: str) -> int:
    rates = ExchangeRates()
    usd_rate = rates[rate].value
    return int(usd_rate)
