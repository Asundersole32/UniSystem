from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Annotated


SECRET_KEY = '3f6ababa03a6edad41a98c10daccace918f71f74eae23ec4a08adce255b174b4'
ALGORITH = 'HS256'

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def get_hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db, user):
    return


def authenticate_user(db_user, login_user, login_password):
    return