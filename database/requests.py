from calendar import Day

from database.models import async_session
from database.models import *
from sqlalchemy import select, update


async def set_user(tg_id, tg_name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id, name=tg_name))
            await session.commit()


async def get_windows():
    async with async_session() as session:
        windows = await session.scalars(select(Windows))
        return windows


async def make_consult(day):
    async with async_session() as session:
        select_day = await session.scalar(select(Windows).where(Windows.day == day))
        select_day.window_free = True
        await session.commit()