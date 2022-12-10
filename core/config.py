from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES  = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SCRET_KEY", cast=str, default="0fa58dd637ba5ce3a9744957dab8856f1102e70f6a4b37aabf3f604e7d1e7e51")