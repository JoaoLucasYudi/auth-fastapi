from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.exceptions import HTTPException
from fastapi import status

from app import schemas
from app.db.models import UserModel
from app.schemas import CreateUser

crypt_context = CryptContext(schemes=['sha256_crypt'])


class UserUseCases:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def user_register(self, user: CreateUser):
        user_model = UserModel(
            name=user.name,
            password=crypt_context.hash(user.password)
        )
        try:
            self.db_session.add(user_model)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User alredy exists'
            )
