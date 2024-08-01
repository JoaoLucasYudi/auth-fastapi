import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.exceptions import HTTPException
from fastapi import status
from jose import jwt, JWTError
from datetime import datetime, timedelta

from app import schemas
from app.db.models import UserModel
from app.schemas import CreateUser


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
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

    def user_login(self, user: CreateUser, expires_in: int = 30):
        user_on_db = self.db_session.query(UserModel).filter_by(name=user.name).first()

        if user_on_db is None or not crypt_context.verify(user.password, user_on_db.password): # type: ignore
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='Invalid name or password'
                    )
        exp = datetime.utcnow() + timedelta(minutes=expires_in)

        payload = {
            'sub': user.name,
            'exp': exp
        }

        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM) # type: ignore

        return {
            'access_token': access_token,
            'expires_in': exp.isoformat()
        }

    def verify_token(self, access_token):
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM]) # type: ignore
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token!'
            )

        user_on_db = self.db_session.query(UserModel).filter_by(name=data['sub']).first()

        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token!'
            )
