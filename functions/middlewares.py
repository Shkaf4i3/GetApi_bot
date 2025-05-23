from typing import Any, Awaitable, Callable, Dict


from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery


class Callbackanswer(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
                       event: CallbackQuery,
                       data: Dict[str, Any]):
        await event.answer()
        return await handler(event, data)
