from typing import TypeVar

from pydantic.main import BaseModel

from app.database.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateBaseSchema = TypeVar("CreateBaseSchema", bound=BaseModel)
UpdateBaseSchema = TypeVar("UpdateBaseSchema", bound=BaseModel)
