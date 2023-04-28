from aiogram.dispatcher.filters import Command
from aiogram import Router
from aiogram.types import Message

from db import get_user_settings, set_user_settings
from gpt import fetch_gpt_response


user_router = Router()

@user_router.message(Command(commands='settings'))
async def cmd_settings(message: Message):
	args = message.text.split()
	if len(args) != 2:
		await message.reply("Please use next format /settings gpt_version (gpt-3.5 or gpt-4)")
		return
	gpt_version = args[1]
	if gpt_version not in {"gpt-3.5", "gpt-4"}:
		await message.reply("Correct value: gpt-3.5, gpt-4")
		return

	await set_user_settings(message.from_user.id, gpt_version)
	await message.reply(f'Settings succes updated: \nGPT version: {gpt_version}')

@user_router.message(lambda message, data: data["is_allowed"])
async def procces_message(message: Message):
	user_settings = await get_user_settings(message.from_user.id)
	if not user_settings:
		gpt_version = "gpt-3.5"
		await set_user_settings(message.from_user.id, gpt_version)
	else:
		gpt_version = user_settings["gpt_version"]
	
	response = await fetch_gpt_response(message.text, gpt_version)
	await message.reply(response, parse_mode="HTML")
	
	