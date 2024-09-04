from sqlalchemy import BigInteger, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine('sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name = mapped_column(String)  # difference



class Windows(Base):
    __tablename__ = 'Windows'
    id: Mapped[int] = mapped_column(primary_key=True)
    day = mapped_column(String)
    date = mapped_column(String)
    time = mapped_column(String)
    window_free = mapped_column(Boolean)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
