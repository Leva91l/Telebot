from sqlalchemy import select

from database.models import *


async def get_all_windows():
    async with async_session() as session:
        windows = await session.scalars(select(Window))

        return windows


async def get_free_windows():
    async with async_session() as session:
        windows = await session.scalars(select(Window).where(Window.status == 'Свободно'))
        print(windows)
        return windows


async def make_consult(day):
    async with async_session() as session:
        select_day = await session.scalar(select(Window).where(Window.day == day[0:2]))
        select_day.status = 'Занято'
        await session.commit()


async def new_user(tg_id, name, number, birthday):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id, name=name, number=number, birthday=birthday))
            await session.commit()


async def new_actualuser(tg_id, name, number, birthday):
    async with async_session() as session:
        session.add(ActualUser(tg_id=tg_id, name=name, number=number, birthday=birthday))
        await session.commit()


async def get_day(day):
    async with async_session() as session:
        my_day = await session.scalars(select(Window).where(Window.id == day))
        return my_day


async def admin_close_window(day):
    async with async_session() as session:
        current_day = await session.scalar(select(Window).where(Window.day == day))
        current_day.status = 'Занято'
        await session.commit()


async def admin_open_window(day):
    async with async_session() as session:
        current_day = await session.scalar(select(Window).where(Window.day == day))
        current_day.status = 'Свободно'
        await session.commit()

async def window_actualuser(day):
    async with async_session() as session:
        users = await session.scalars(select(ActualUser).order_by(ActualUser.id.desc()))
        actual_user = users.first().id
        select_day = await session.scalar(select(Window).where(Window.day == day))
        select_day.actualuser_id = actual_user
        await session.commit()