import os
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from config import POSTGRES_URI
from models import Base, UserSettings


engine = create_async_engine(POSTGRES_URI)


async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_user_settings(user_id: int):
    async with AsyncSession(engine) as session:
        result = session.execut(
            "SELECT gpt_version FROM user_settings WHERE user_id=:user_id",
            {"user_id": user_id},
        )
        row = result.fetchone()
        return {"gpt_version": row[0]} if row else None


async def set_user_settings(user_id: int, gpt_version: str):
    async with AsyncSession(engine) as session:
        stmt = (
            UserSettings.__table__.insert()
            .values(user_id=user_id, gpt_version=gpt_version)
            .on_conflict_do_update(
                constrain=UserSettings.__table__.primary_key,
                set_={"gpt_version": gpt_version},
            )
        )

        await session.execute(stmt)
        await session.commit()
