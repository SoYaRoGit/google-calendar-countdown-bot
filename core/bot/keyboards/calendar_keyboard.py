from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import config



async def builder_inline_calendar_title():
    inline_calendar_title = InlineKeyboardBuilder()
    for cal_id, cal_name in config.calendar.calendars.items():
        inline_calendar_title.add(
            InlineKeyboardButton(
                text=cal_name,
                callback_data=cal_id
            )
        )
    inline_calendar_title.adjust(1)
    return inline_calendar_title.as_markup()