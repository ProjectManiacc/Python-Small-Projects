import yagmail
import pandas as ps
import datetime
import time
from news import NewsFeed


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today, )
    email = yagmail.SMTP(user='python.automated.emails1@gmail.com', password='iyhtcdnhwygdokzx')
    email.send(to=row['email'],
               subject=f'Your {row["interest"]} news for today!',
               contents=f"Hello {row['name']}.\n See what's on about {row['interest']} today.\n\n {news_feed.get()}\nPiotrek")


while True:
    if datetime.datetime.now().hour == 6 and datetime.datetime.now().minute == 00:

        df = ps.read_excel('people.xlsx')
        for index,row in df.iterrows():
            send_email()

    time.sleep(60)