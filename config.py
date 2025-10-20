from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


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


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


config = Settings()