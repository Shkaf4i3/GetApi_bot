from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import reply as kb
from functions.api_func import get_city_world, get_cryptocurrency_rate, get_currency_rate
from functions.calldata_api import Checkcryptodata, Checkcurrencydata


admin = Router()

class Weather(StatesGroup):
    city_ru = State()
    city_us = State()
    city_uk = State()
    city_ua = State()


@admin.message(CommandStart())
async def start_message(message: Message):
    await message.answer(f'❤️ Привет, {message.from_user.first_name} ❤️\n'
                         'Здесь ты сможешь узнать любую доступную информацию по API 🕸\n'
                         '\n'
                         '👇 Для продолжения работы воспользуйся меню 👇',
                         reply_markup=kb.main_kb())

@admin.message(Command('help'))
async def help_message(message: Message):
    await message.answer('Данный бот - сборщик информации, использующий API \n'
                         'Для обратной связи 👉- @shkaf4i3',
                         reply_markup=kb.back_main_kb())

@admin.message(F.text == '⚡️ Вернуться в меню ⚡️')
async def back_main_menu(message: Message):
    await message.answer('Вы вернулись в меню',
                         reply_markup=kb.main_kb())

@admin.message(F.text == '📊 Курсы валют 📊')
async def currency_rates_menu(message: Message):
    await message.answer('Какие курсы валют вас интересуют?',
                         reply_markup=await kb.exchange_rates())

@admin.message(F.text == '🖥 Курсы криптовалют 🖥')
async def cryptocurrency_rates(message: Message):
    await message.answer('Какие курсы криптовалют вас интересуют?',
                         reply_markup=await kb.exchange_crypto_rates())

@admin.message(F.text == '🌆 Информация о погоде 🌆')
async def weather_info(message: Message):
    await message.answer('Какая страна вас интересует?',
                         reply_markup=await kb.info_weather())


@admin.callback_query(F.data == 'info_rf')
async def city_rf_weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Weather.city_ru)

    await callback.message.answer('Введите название города')

@admin.message(Weather.city_ru)
async def response_city_ru(message: Message, state: FSMContext):
    await state.update_data(city_ru=message.text)
    data = await state.get_data()
    city = data['city_ru']
    response_sity = await get_city_world(city, 'RU')

    if response_sity:
        await message.answer(f'Погода в городе "{city}" - {response_sity} °C',
                             reply_markup=kb.main_kb())
    else:
        await message.answer('Произошла ошибка при запросе, попробуйте еще раз \n'
                             'Возможно, вы указали неверный город',
                             reply_markup=kb.main_kb())
    await state.clear()


@admin.callback_query(F.data == 'info_us')
async def city_us_weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Weather.city_us)

    await callback.message.answer('Введите название штата')

@admin.message(Weather.city_us)
async def response_city_us(message: Message, state: FSMContext):
    await state.update_data(city_us=message.text)
    data = await state.get_data()
    city = data['city_us']
    response_city = await get_city_world(city, 'US')

    if response_city:
        await message.answer(f'Погода в штате "{city}" - {response_city} °C',
                             reply_markup=kb.main_kb())
    else:
        await message.answer('Произошла ошибка при запросе, попробуйте еще раз \n'
                             'Возможно, вы указали неверный штат',
                             reply_markup=kb.main_kb())
    await state.clear()


@admin.callback_query(F.data == 'info_uk')
async def city_uk_weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Weather.city_uk)

    await callback.message.answer('Введите название города')

@admin.message(Weather.city_uk)
async def response_city_uk(message: Message, state: FSMContext):
    await state.update_data(city_uk=message.text)
    data = await state.get_data()
    city = data['city_uk']
    response_city = await get_city_world(city, 'UK')

    if response_city:
        await message.answer(f'Погода в городе "{city}" - {response_city} °C',
                             reply_markup=kb.main_kb())
    else:
        await message.answer('Произошла ошибка при запросе, попробуйте еще раз \n'
                             'Возможно, вы указали неверный город',
                             reply_markup=kb.main_kb())
    await state.clear()


@admin.callback_query(F.data == 'info_ua')
async def city_ua_weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Weather.city_ua)

    await callback.message.answer('Введите название города')

@admin.message(Weather.city_ua)
async def response_city_ua(message: Message, state: FSMContext):
    await state.update_data(city_ua=message.text)
    data = await state.get_data()
    city = data['city_ua']
    response_city = await get_city_world(city, 'UA')

    if response_city:
        await message.answer(f'Погода в городе "{city}" - {response_city} °C',
                             reply_markup=kb.main_kb())
    else:
        await message.answer('Произошла ошибка при запросе, попробуйте еще раз \n'
                             'Возможно, вы указали неверный город',
                             reply_markup=kb.main_kb())
    await state.clear()


@admin.callback_query(Checkcryptodata.filter())
async def crypto_rates(callback: CallbackQuery, callback_data: Checkcryptodata) -> None:
    if callback_data.rate == 'btc':
        btc_data = await get_cryptocurrency_rate(1)
        await callback.message.answer(f'Текущий курс Bitcoin - {btc_data} долларов')
    elif callback_data.rate == 'teh':
        not_data = await get_cryptocurrency_rate(16)
        await callback.message.answer(f'Текущий курс Tether USDT - {not_data} долларов')
    elif callback_data.rate == 'solana':
        solana_data = await get_cryptocurrency_rate(5663)
        await callback.message.answer(f'Текущий курс Solana - {solana_data} долларов')
    elif callback_data.rate == 'eth':
        eth_data = await get_cryptocurrency_rate(3)
        await callback.message.answer(f'Текущий курс ETH - {eth_data} долларов')


@admin.callback_query(Checkcurrencydata.filter())
async def currency_rates(callback: CallbackQuery, callback_data: Checkcurrencydata) -> None:
    if callback_data.rate == 'usd':
        usd_rate = get_currency_rate('USD')
        await callback.message.answer(f'Сейчас курс доллара - {usd_rate} рублей')
    elif callback_data.rate == 'eur':
        eur_rate = get_currency_rate('EUR')
        await callback.message.answer(f'Сейчас курс евро - {eur_rate} рублей')
    elif callback_data.rate == 'uah':
        uah_rate = get_currency_rate('UAH')
        await callback.message.answer(f'Сейчас курс гривны - {uah_rate} рублей')
