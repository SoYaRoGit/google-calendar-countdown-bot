from aiogram import Router, types
from aiogram.filters.command import CommandStart
from core.bot.language.language_ru import LANGUAGE_RU


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """Стартовый обработчик на команду /start"""
    user = message.from_user

    await message.delete()
    await message.answer(
        text=LANGUAGE_RU["command_start_handler"].format(user.full_name)
    )


