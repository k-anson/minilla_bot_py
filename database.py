from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

Base = declarative_base()

class Calendar(Base):
  __tablename__= 'calendars'

  id = Column(Integer, primary_key=True)
  guild_id = Column(String(length=18))
  channel_id = Column(String(length=18))
  events_channel_id = Column(String(length=18))
  message_id = Column(String(length=18))
  events = relationship('Event')

class Event(Base):
  __tablename__= 'events'

  id = Column(Integer, primary_key=True)
  name = Column(String(length=255))
  date = Column(DateTime)
  description = Column(String(length=255))
  message_id = Column(String(length=18))
  calendar_id = Column(Integer, ForeignKey('calendars.id'))
  calendar = relationship('Calendar', back_populates='events')
  owner_id = Column(Integer, ForeignKey('attendees.id'))

class Database:
  session:Session
  Calendar = Calendar
  Event = Event

  def __init__(self, config):
    engine = create_engine(f'mysql+pymysql://{config["DATABASE_USERNAME"]}:{config["DATABASE_PASSWORD"]}@{config["DATABASE_HOST"]}:{config["DATABASE_PORT"]}/{config["DATABASE_NAME"]}')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    self.session = Session()