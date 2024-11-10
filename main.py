from asyncio import run
from logging import basicConfig, INFO

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from functions.commands import private
from handlers.admin_private import admin
from functions.config_reader import config


async def main() -> None:
    bot = Bot(token=config.bot_token.get_secret_value(),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_routers(admin)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)



if __name__ == '__main__':
    basicConfig(level=INFO)
    try:
        run(main())
    except KeyboardInterrupt:
        print('Exit')
