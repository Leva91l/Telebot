import time
from datetime import datetime, date, timedelta

from sqlalchemy import create_engine, update

from database.models import Window

engine = create_engine('sqlite:////home/nikolay/PycharmProjects/TeleBot/db.sqlite3')
engine.connect()
while True:
    weekday = int(datetime.today().weekday())
    now = date.today()
    week = timedelta(days=6)
    new_date = now + week
    new_date = new_date.strftime('%d.%m.%Y')
    with engine.begin() as connection:
        if weekday == 0:
            connection.execute(update(Window).where(Window.id == 7).values(status='Свободно', date=new_date))
        else:
            connection.execute(update(Window).where(Window.id == weekday).values(status='Свободно'))
            connection.execute(update(Window).where(Window.id == weekday).values(date=new_date))

    time.sleep(86400)
