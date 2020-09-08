from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

Base = declarative_base()

class Calendar(Base):
  __tablename__= 'calendars'

  id = Column('id', Integer, primary_key=True)
  channel_id = Column('channel_id', Integer)
  events_channel_id = Column('events_channel_id', Integer)
  message_id = Column('message_id', Integer)

class Event(Base):
  __tablename__= 'events'

  id = Column('id', Integer, primary_key=True)
  name = Column('name', String(length=255))
  date = Column('date', DateTime)
  description = Column('description', String(length=255))
  message_id = Column('message_id', Integer)

class Database:
  session:Session
  Calendar = Calendar
  Event = Event

  def __init__(self, config):
    engine = create_engine(f'mysql+pymysql://{config["DATABASE_USERNAME"]}:{config["DATABASE_PASSWORD"]}@{config["DATABASE_HOST"]}:{config["DATABASE_PORT"]}/{config["DATABASE_NAME"]}', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    self.session = Session()