from typing import List
import datetime

from models.user import User, UserIn
from core.security import hash_password
from db.users import users
from .base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all_(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)
    

    async def get_by_id(self, id: int) -> User:
        query = users.select().where(users.c.id==id).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
    

    async def create(self, u: UserIn) -> User:
        user = User(
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("id", None)

        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    
    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id=id,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            updated_at=datetime.datatime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = users.update().where(user.c.id==id).values(**values)
        await self.database.execute(query)
        return user


    
    async def get_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email==email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)