from sqlalchemy import select

from database.models import *


async def get_all_windows():
    async with async_session() as session:
        windows = await session.scalars(select(Window))
        print(windows)
        print('1')
        return windows


async def get_admin_schedule():
    async with async_session() as session:
        schedule = await session.scalars(select(Window).where(Window.actualuser_id))
        return schedule

async def get_free_windows():
    async with async_session() as session:
        windows = await session.scalars(select(Window).where(Window.status == 'Свободно'))
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


async def get_info_about_actualuser(day):
    async with async_session() as session:
        current_day = await session.scalar(select(Window).where(Window.day == day))
        actual_user_id = current_day.actualuser_id
        actual_user = await session.scalar(select(ActualUser).where(ActualUser.id == actual_user_id))
        return actual_user


async def admin_close_window(day):
    async with async_session() as session:
        current_day = await session.scalar(select(Window).where(Window.day == day))
        current_day.status = 'Занято'
        await session.commit()


async def admin_open_window(day):
    async with async_session() as session:
        current_day = await session.scalar(select(Window).where(Window.day == day))
        actual_user = current_day.actualuser_id
        current_day.status = 'Свободно'
        current_day.actualuser_id = None
        user = await session.scalar(select(ActualUser).where(ActualUser.id == actual_user))
        try:
            await session.delete(user)
        except:
            pass
        await session.commit()


async def window_actualuser(day):
    async with async_session() as session:
        users = await session.scalars(select(ActualUser).order_by(ActualUser.id.desc()))
        actual_user = users.first().id
        select_day = await session.scalar(select(Window).where(Window.day == day))
        select_day.actualuser_id = actual_user
        await session.commit()
