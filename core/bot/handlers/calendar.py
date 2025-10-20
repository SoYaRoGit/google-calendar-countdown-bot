from aiogram import Router, types
from aiogram.filters import Command
from core.bot.services.google_calendar import google_calendar_api
from core.bot.keyboards.calendar_keyboard import builder_inline_calendar_title



router = Router()


@router.message(Command("calendar"))
async def show_calendar_choice(message: types.Message):
    """Показывает inline-кнопки с выбором календаря."""
    keyboard = await builder_inline_calendar_title()
    await message.answer("Выберите календарь:", reply_markup=keyboard)


@router.callback_query(lambda c: c.data.startswith(""))
async def handle_calendar_choice(callback: types.CallbackQuery):
    calendar_id = callback.data
    try:
        events_text = google_calendar_api.get_event_list(calendar_id)
        await callback.message.edit_text(
            f"📅 События из календаря:\n\n{events_text}",
            reply_markup=None
        )
    except Exception as e:
        await callback.message.edit_text("❌ Ошибка при загрузке календаря.")
    await callback.answer()