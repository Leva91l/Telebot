from sqlalchemy import select
from sqlalchemy.orm import defer

from database.models import *


async def get_windows():
    async with async_session() as session:
        windows = await session.scalars(select(Windows).where(Windows.status == 'Свободно'))
        return windows


async def make_consult(day):
    async with async_session() as session:
        select_day = await session.scalar(select(Windows).where(Windows.day == day[0:2]))
        select_day.status = 'Занято'
        await session.commit()


async def new_user(tg_id, name, number, birthday):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id, name=name, number=number, birthday=birthday))
            await session.commit()


async def get_day(day):
    async with async_session() as session:
        my_day = await session.scalars(select(Windows).where(Windows.id == day))
        return my_day