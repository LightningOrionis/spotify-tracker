from typing import TypeVar

from app.database.base_class import Base
from pydantic.main import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateBaseSchema = TypeVar("CreateBaseSchema", bound=BaseModel)
UpdateBaseSchema = TypeVar("UpdateBaseSchema", bound=BaseModel)
