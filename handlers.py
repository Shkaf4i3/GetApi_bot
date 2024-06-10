from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import reply as kb
from functions import (get_city_world,
                       get_cryptocurrency_rate,
                       get_currency_rate)


user_private_router = Router()

class Weather(StatesGroup):
    city_ru = State()
    city_us = State()
    city_uk = State()
    city_ua = State()


@user_private_router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(f'❤️ Привет, {message.from_user.first_name} ❤️\n'
                         'Здесь ты сможешь узнать любую доступную информацию по API 🕸\n'
                         '\n'
                         '👇 Для продолжения работы воспользуйся меню 👇',
                         reply_markup=kb.main_kb())

@user_private_router.message(Command('help'))
async def help_message(message: Message):
    await message.answer('Данный бот - сборщик информации, использующий API \n'
                         'Для обратной связи 👉- @shkaf4i3',
                         reply_markup=kb.back_main_kb())

@user_private_router.message(F.text == '⚡️ Вернуться в меню ⚡️')
async def back_main_menu(message: Message):
    await message.answer('Вы вернулись в меню',
                         reply_markup=kb.main_kb())

@user_private_router.message(F.text == '📊 Курсы валют 📊')
async def currency_rates(message: Message):
    await message.answer('Какие курсы валют вас интересуют?',
                         reply_markup=await kb.exchange_rates())

@user_private_router.message(F.text == '🖥 Курсы криптовалют 🖥')
async def cryptocurrency_rates(message: Message):
    await message.answer('Какие курсы криптовалют вас интересуют?',
                         reply_markup=await kb.exchange_crypto_rates())

@user_private_router.message(F.text == '🌆 Информация о погоде 🌆')
async def weather_info(message: Message):
    await message.answer('Какая страна вас интересует?',
                         reply_markup=await kb.info_weather())




@user_private_router.callback_query(F.data == 'info_rf')
async def city_rf_weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Weather.city_ru)

    await callback.answer()
    await callback.message.answer('Введите название города')

@user_private_router.message(Weather.city_ru)
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


@user_private_router.callback_query(F.data == 'info_us')
async def city_us_weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Weather.city_us)

    await callback.answer()
    await callback.message.answer('Введите название штата')

@user_private_router.message(Weather.city_us)
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


@user_private_router.callback_query(F.data == 'info_uk')
async def city_uk_weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Weather.city_uk)

    await callback.answer()
    await callback.message.answer('Введите название города')

@user_private_router.message(Weather.city_uk)
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


@user_private_router.callback_query(F.data == 'info_ua')
async def city_ua_weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Weather.city_ua)

    await callback.answer()
    await callback.message.answer('Введите название города')

@user_private_router.message(Weather.city_ua)
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


@user_private_router.callback_query(F.data == 'btc_rate')
async def btc_rate(callback: CallbackQuery):
    btc_data = await get_cryptocurrency_rate(0)
    await callback.answer()
    await callback.message.answer(f'Курс Bitcoin - {btc_data} долларов')

@user_private_router.callback_query(F.data == 'ton_rate')
async def ltc_rate(callback: CallbackQuery):
    not_data = await get_cryptocurrency_rate(9)
    await callback.answer()
    await callback.message.answer(f'Курс Notcoin - {not_data} долларов')

@user_private_router.callback_query(F.data == 'solana_rate')
async def usdt_rate(callback: CallbackQuery):
    solana_data = await get_cryptocurrency_rate(4)
    await callback.answer()
    await callback.message.answer(f'Курс Solana - {solana_data} долларов')

@user_private_router.callback_query(F.data == 'eth_rate')
async def eth_rate(callback: CallbackQuery):
    eth_data = await get_cryptocurrency_rate(1)
    await callback.answer()
    await callback.message.answer(f'Курс ETH - {eth_data} долларов')


@user_private_router.callback_query(F.data == 'usd_rate')
async def check_usd(callback: CallbackQuery):
    usd_rate = get_currency_rate('USD')

    await callback.answer()
    await callback.message.answer(f'Сейчас курс доллара - {usd_rate} рублей')

@user_private_router.callback_query(F.data == 'eur_rate')
async def check_eur(callback: CallbackQuery):
    eur_rate = get_currency_rate('EUR')

    await callback.answer()
    await callback.message.answer(f'Сейчас курс евро - {eur_rate} рублей')

@user_private_router.callback_query(F.data == 'uah_rate')
async def check_uah(callback: CallbackQuery):
    uah_rate = get_currency_rate('UAH')

    await callback.answer()
    await callback.message.answer(f'Сейчас курс гривны - {uah_rate} рублей')
