from typing import Any, Dict, Generic, List, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.schemas.base import CreateBaseSchema, ModelType, UpdateBaseSchema


class BaseCRUD(Generic[ModelType, CreateBaseSchema, UpdateBaseSchema]):  # type: ignore
    def __init__(self, model: ModelType):
        self.model = model

    def get(self, session: Session, id: int) -> ModelType:
        obj = session.query(self.model).get(id)
        return obj

    def get_by_offset_and_limit(self, session: Session, offset: int = 0, limit: int = 100) -> List[ModelType]:
        objects = session.query(self.model).offset(offset).limit(limit).all()
        return objects

    def get_all(self, session: Session):
        objects = session.query(self.model).all()
        return objects

    def create(self, session: Session, obj_to_add: CreateBaseSchema) -> ModelType:
        obj = self.model(**obj_to_add)

        session.add(obj)
        session.commit()
        session.refresh(obj)

        return obj

    def update(
        self, session: Session, obj_to_update: ModelType, update_data: Union[UpdateBaseSchema, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(obj_to_update)

        if not isinstance(update_data, dict):
            update_data = update_data.dict(exclude_unset=True)

        for field in update_data:
            if field in obj_data:
                setattr(obj_to_update, field, update_data[field])

        session.add(obj_to_update)
        session.commit()
        session.refresh(obj_to_update)

        return obj_to_update

    def delete(self, session: Session, id: int) -> ModelType:
        obj = session.query(self.model).get(id)

        session.delete(obj)
        session.commit()

        return obj
