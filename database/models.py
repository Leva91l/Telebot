from sqlalchemy import BigInteger, String, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
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
    number = mapped_column(String)
    birthday = mapped_column(String)



class ActualUser(Base):
    __tablename__ = 'actualusers'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name = mapped_column(String)
    number = mapped_column(String)
    birthday = mapped_column(String)
    window = relationship('Window', back_populates='actualuser')

class Window(Base):
    __tablename__ = 'windows'
    id: Mapped[int] = mapped_column(primary_key=True)
    day = mapped_column(String)
    date = mapped_column(String)
    time = mapped_column(String)
    status = mapped_column(String)
    actualuser = relationship('ActualUser', back_populates='window')
    actualuser_id = mapped_column(ForeignKey('actualusers.id'))




async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)




