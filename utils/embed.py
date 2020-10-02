from discord import Embed, Color
from datetime import date, datetime, timedelta
from typing import List

from database import Database

def create_cal_embed(db:Database) -> Embed:
  embed = Embed(
    color = Color.blue(),
    title = ':calendar_spiral: Upcoming Events'
  )
  # embed.add_field(name='​\u200b', value='\u200b', inline=False)

  # Today's events
  context_date = date.today()
  events:List[Database.Event] = db.session.query(db.Event).filter(db.Event.date.between(context_date, context_date + timedelta(1))).all()
  if events:
    embed_value = ''
    for event in events:
      embed_value = embed_value + f'\n{event_printout(event)}'
    embed.add_field(name=f"Today\n{context_date.strftime('%A, %B %d')}\u2003", value=embed_value, inline=False)

  # Tomorrow's events
  context_date += timedelta(1)
  events = db.session.query(db.Event).filter(db.Event.date.between(context_date, context_date + timedelta(1))).all()
  if events:
    embed_value = ''
    for event in events:
      embed_value = embed_value + f'\n{event_printout(event)}'
    embed.add_field(name=f"Tomorrow\n{context_date.strftime('%A, %B %d')}\u2003", value=embed_value, inline=False)

  # Loop over next 26 days
  for i in range(26):
    context_date += timedelta(1)
    events = db.session.query(db.Event).filter(db.Event.date.between(context_date, context_date + timedelta(1))).all()
    if events:
      embed_value = ''
      for event in events:
        embed_value = embed_value + f'\n{event_printout(event)}'
      embed.add_field(name=context_date.strftime('%A, %B %d'), value=embed_value, inline=False)

  embed.set_footer(text=f"Last updated - {datetime.today().strftime('%A, %B %d at %-I:%M %p')}")

  return embed

def event_printout(event:Database.Event):
  # event_datetime = datetime(event.date)
  return f"**{event.date.strftime('%-I:%M %p')}**: [{event.name}](https://discordapp.com/channels/{event.calendar.guild_id}/{event.calendar.events_channel_id}/{event.message_id}) - _0 attendees_"

def create_calevent_embed(db:Database, event:Database.Event) -> Embed:
  embed = Embed(
    color = Color.blue(),
    title = f':calendar_spiral: {event.name}'
  )
  embed.add_field(name='Date', value=event.date.strftime('%A, %B %d at %-I:%M %p'), inline=False)
  embed.add_field(name='Description', value=event.description, inline=False)

  return embed