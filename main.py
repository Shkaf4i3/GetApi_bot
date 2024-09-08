from asyncio import run
from logging import basicConfig, INFO
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from commands import private
from handlers import user_private_router


async def main() -> None:
    load_dotenv()
    bot = Bot(token=getenv('bot_token'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_routers(user_private_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)



if __name__ == '__main__':
    basicConfig(level=INFO)
    try:
        run(main())
    except KeyboardInterrupt:
        print('Exit')
