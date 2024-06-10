from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


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
    inline_keyboard.button(text='💵 Курс USD 💵', callback_data='usd_rate')
    inline_keyboard.button(text='💶 Курс EUR 💶', callback_data='eur_rate')
    inline_keyboard.button(text='💸 Курс UAH 💸', callback_data='uah_rate')
    return inline_keyboard.adjust(1).as_markup()

async def exchange_crypto_rates() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.button(text='Курс Bitcoin', callback_data='btc_rate')
    inline_keyboard.button(text='Курс Toncoin', callback_data='ton_rate')
    inline_keyboard.button(text='Курс Solana', callback_data='solana_rate')
    inline_keyboard.button(text='Курс ETH', callback_data='eth_rate')
    return inline_keyboard.adjust(1).as_markup()

async def info_weather() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.button(text='🇷🇺 Информация по городам РФ 🇷🇺',callback_data='info_rf')
    inline_keyboard.button(text='🇺🇸 Информация по городам США 🇺🇸', callback_data='info_us')
    inline_keyboard.button(text='🇬🇧 Информация по городам Англии 🇬🇧', callback_data='info_uk')
    inline_keyboard.button(text='🇺🇦 Информация по городам Украины 🇺🇦', callback_data='info_ua')
    return inline_keyboard.adjust(2).as_markup()
