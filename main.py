from asyncio import gather, run
from core.bot.config import start_bot


async def main() -> None:
    await gather(start_bot())


if __name__ == "__main__":
    try:
        run(main())
    except KeyboardInterrupt:
        print("Программа принудительна завершена!")
