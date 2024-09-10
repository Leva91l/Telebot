import time
from datetime import datetime

from sqlalchemy import create_engine, update

from database.models import Windows

engine = create_engine('sqlite:////home/nikolay/PycharmProjects/TeleBot/db.sqlite3')
engine.connect()
while True:
    print(datetime.now().weekday())
    current_date_now = int(datetime.today().weekday())
    with engine.begin() as connection:
        if current_date_now == 0:
            connection.execute(update(Windows).where(Windows.id == 7).values(status='Свободно'))
        else:
            connection.execute(update(Windows).where(Windows.id == 1).values(status='Свободно'))

    time.sleep(86400)
