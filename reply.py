from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from functions.calldata_api import Checkcryptodata, Checkcurrencydata


def main_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='📊 Курсы валют 📊')
    keyboard.button(text='🖥 Курсы криптовалют 🖥')
    keyboard.button(text='🌆 Информация о погоде 🌆')
    return keyboard.adjust(2).as_markup(resize_keyboard=True)

def back_main_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='⚡️ Вернуться в меню ⚡️')
    return keyboard.as_markup(resize_keyboard=True)



async def exchange_rates() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.button(text='💵 USD 💵', callback_data=Checkcurrencydata(rate='usd'))
    inline_keyboard.button(text='💶 EUR 💶', callback_data=Checkcurrencydata(rate='eur'))
    inline_keyboard.button(text='💸 UAH 💸', callback_data=Checkcurrencydata(rate='uah'))
    return inline_keyboard.adjust(1).as_markup()

async def exchange_crypto_rates() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.button(text='Bitcoin', callback_data=Checkcryptodata(rate='btc'))
    inline_keyboard.button(text='Tether', callback_data=Checkcryptodata(rate='teh'))
    inline_keyboard.button(text='Solana', callback_data=Checkcryptodata(rate='solana'))
    inline_keyboard.button(text='ETH', callback_data=Checkcryptodata(rate='eth'))
    return inline_keyboard.adjust(1).as_markup()

async def info_weather() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.button(text='🇷🇺 Информация по городам РФ 🇷🇺',callback_data='info_rf')
    inline_keyboard.button(text='🇺🇸 Информация по городам США 🇺🇸', callback_data='info_us')
    inline_keyboard.button(text='🇬🇧 Информация по городам Англии 🇬🇧', callback_data='info_uk')
    inline_keyboard.button(text='🇺🇦 Информация по городам Украины 🇺🇦', callback_data='info_ua')
    return inline_keyboard.adjust(2).as_markup()
