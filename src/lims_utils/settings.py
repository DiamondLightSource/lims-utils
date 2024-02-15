import json
import os
from pathlib import Path
from typing import Any, Dict, Literal, Tuple, Type

from pydantic import BaseModel
from pydantic.fields import FieldInfo
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)


class Auth(BaseModel):
    endpoint: str = "https://localhost/auth"
    type: Literal["dummy", "micro"] = "micro"
    cookie_key: str = "cookie_key"


class DB(BaseModel):
    pool: int = 3
    overflow: int = 6


class JsonConfigSettingsSource(PydanticBaseSettingsSource):
    """Reads application settings from JSON file"""

    def get_field_value(
        self, field: FieldInfo, field_name: str
    ) -> Tuple[Any, str, bool]:
        encoding = self.config.get("env_file_encoding")
        file_content_json = json.loads(
            Path(os.environ.get("CONFIG_PATH") or "config.json").read_text(encoding)
        )
        field_value = file_content_json.get(field_name)
        return field_value, field_name, False

    def prepare_field_value(
        self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool
    ) -> Any:
        return value

    def __call__(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}

        for field_name, field in self.settings_cls.model_fields.items():
            field_value, field_key, value_is_complex = self.get_field_value(
                field, field_name
            )
            field_value = self.prepare_field_value(
                field_name, field, field_value, value_is_complex
            )
            if field_value is not None:
                d[field_key] = field_value

        return d


class Settings(BaseSettings):
    """Base settings for application"""

    model_config = SettingsConfigDict(env_file_encoding="utf-8")

    auth: Auth = Auth()
    db: DB = DB()

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            JsonConfigSettingsSource(settings_cls),
        )
