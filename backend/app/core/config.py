import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "Fastapi_Ecommerce"
    PROJECT_VERSION: str = "1.0.0"
    USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = "postgresql://ehhsctbn:zaX8oRbkyifRm67LKkaRWlnvNA5L1yaW@rain.db.elephantsql.com/ehhsctbn"

    JWT_PUBLIC_KEY: str = os.getenv("JWT_PUBLIC_KEY")
    JWT_PRIVATE_KEY: str = os.getenv("JWT_PRIVATE_KEY")
    REFRESH_TOKEN_EXPIRES_IN: int = os.getenv("REFRESH_TOKEN_EXPIRES_IN")
    ACCESS_TOKEN_EXPIRES_IN: int = os.getenv("ACCESS_TOKEN_EXPIRES_IN")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")

    RAJAONGKIR_API = os.getenv("RAJAONGKIR_API")
    MIDTRANS_SERVER_KEY = os.getenv("MIDTRANS_SERVER_KEY")
    MIDTRANS_CLIENT_KEY = os.getenv("MIDTRANS_CLIENT_KEY")
    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_SECRET_KEY = os.getenv("CLOUDINARY_SECRET_KEY")


settings = Settings()
