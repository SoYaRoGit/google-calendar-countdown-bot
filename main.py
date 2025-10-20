from asyncio import gather, run


async def main() -> None:
    ...


if __name__ == "__main__":
    try:
        run(main())
    except KeyboardInterrupt:
        print("Программа принудительна завершена!")
