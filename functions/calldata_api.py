from aiogram.filters.callback_data import CallbackData


class Checkcryptodata(CallbackData, prefix='rate', sep='_'):
    rate: str


class Checkcurrencydata(CallbackData, prefix='currency', sep='_'):
    rate: str
