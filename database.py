from peewee import *
from peewee import PeeweeException

_db = SqliteDatabase('telegram_client_data')


class Base(Model):
    class Meta:
        database = _db


class Event(Base):
    user_id = IntegerField()
    name = CharField()
    time = TimestampField()
    status = BooleanField()


def select_all_names():
    users = {}
    for event in Event.select():
        if event.user_id not in users:
            users[event.user_id] = event
    return users


def initialize(drop=False):
    _db.connect()
    try:
        if drop:
            _db.drop_tables(Base.__subclasses__(), safe=True)
        _db.create_tables(Base.__subclasses__())
    except PeeweeException:
        pass


if __name__ == '__main__':
    initialize(drop=True)
