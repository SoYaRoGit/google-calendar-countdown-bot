from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Dict

DEFAULT_SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
DEFAULT_SERVICE_ACCOUNT_FILE = "google-calendar-key.json"

class GoogleCalendarAPI(BaseSettings):
    calendars: Dict[str, str] = Field(default_factory=dict)
    scopes: list[str] = Field(default=DEFAULT_SCOPES)
    service_account_file: str = Field(default=DEFAULT_SERVICE_ACCOUNT_FILE)


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="CALENDAR_API_",
        extra="ignore"
    )
    

class TelegramBotSettings(BaseSettings):
    token: str
    protect_content: bool

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="TELEGRAM_BOT_",
        extra="ignore"
    )


class Settings(BaseSettings):
    bot: TelegramBotSettings = Field(default_factory=TelegramBotSettings)
    calendar: GoogleCalendarAPI = Field(default_factory=GoogleCalendarAPI)


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


config = Settings()