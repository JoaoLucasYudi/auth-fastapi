from app.db.connection import SessionLocal


def get_db_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close() # type: ignore
