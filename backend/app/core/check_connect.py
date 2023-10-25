from databases import Database
from .database import SQLALCHAMY_DATABASE_URL

async def check_db_connected():
    try:
        if not str(SQLALCHAMY_DATABASE_URL).__contains__("sqlite"):
            db = Database(SQLALCHAMY_DATABASE_URL)
            if not db.is_connected:
                await db.connect()
                await db.execute("SELECT 1")
        print("Database is connected")
    except Exception as e:
        print("Database is not connected")
        raise e

async def check_db_disconnected():
    try:
        if not str(SQLALCHAMY_DATABASE_URL).__contains__("sqlite"):
            db = Database(SQLALCHAMY_DATABASE_URL)
            if db.is_connected:
                await db.disconnect()
                await db.execute("SELECT 1")
        print("Database is disconnected")
    except Exception as e:
        print("Database is not disconnected")
        raise e