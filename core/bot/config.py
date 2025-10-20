from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from config import config


bot = Bot(
    token=config.bot.token,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        protect_content=config.bot.protect_content
    )
)

dispatcher = Dispatcher()


@dispatcher.startup()
async def startup() -> None:
    """Стартовый обработчик при запуске бота"""
    print("Бот успешно запущен!")


@dispatcher.shutdown()
async def shutdown() -> None:
    """Последний на очереди обработчик перед выключением бота"""
    print("Бот успешно выключен!")


async def include_router() -> None:
    """Функция подключения внешний роутеров"""
    ...

async def start_bot() -> None:
    await include_router()
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)