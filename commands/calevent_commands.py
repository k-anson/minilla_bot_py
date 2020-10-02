from discord.ext import commands
from discord.ext.commands import Bot, Context, CommandError
from datetime import datetime, date
from dateutil.parser import parse

from database import Database
from utils.embed import create_cal_embed, create_calevent_embed

def create_calevent_commands(config:dict, client:Bot, db:Database):
  @client.group(invoke_without_command=True)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def calevent(ctx:Context):
    # TODO: send tooltip
    pass

  @calevent.command(name='create')
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def calevent_create(ctx:Context, name:str, event_datetime:convert_to_datetime, description:str):
    calendar:db.Calendar = db.session.query(db.Calendar).filter(db.Calendar.guild_id == ctx.guild.id).first()
    event = db.Event(
      name = name,
      date = event_datetime,
      description = description,
      calendar_id = calendar.id
    )
    db.session.add(event)
    db.session.commit()

    channel = client.get_channel(int(calendar.events_channel_id))
    message = await channel.send(embed=create_calevent_embed(db, event))
    event.message_id = message.id
    db.session.commit()
    await ctx.send(f'Event "{event.name}" created')

    channel = client.get_channel(int(calendar.channel_id))
    message = await channel.fetch_message(int(calendar.message_id))
    await message.edit(embed=create_cal_embed(db))

  @calevent.error
  @calevent_create.error
  async def calevent_error(ctx:Context, error:CommandError):
    if isinstance(error, commands.NoPrivateMessage):
      pass
    else:
      await ctx.send(error)

def convert_to_datetime(arg):
  return parse(arg)