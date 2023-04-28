from aiogram import types
from aiogram import BaseMiddleware
from config import ALLOWED_USERS


class CheckUserMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        if message.from_user.id in ALLOWED_USERS:
            data["is_allowed"] = True

        else:
            data["is_allowed"] = False
            await message.reply("Sorry access deny")
