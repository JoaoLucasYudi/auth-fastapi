from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

from app.auth_user import UserUseCases
from app.db.connection import SessionLocal


oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')

def get_db_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close() # type: ignore

def token_verifier(
    db_session: Session = Depends(get_db_session),
    token = Depends(oauth_scheme)
):
    uc = UserUseCases(db_session=db_session)
    uc.verify_token(access_token=token)
