import discord
from discord.ext import commands
from discord.ext.commands import Bot, Context, CommandError
from discord import TextChannel

from database import Database
from utils.embed import create_cal_embed

def create_cal_commands(config:dict, client:Bot, db:Database):
  @client.group(invoke_without_command=True)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def cal(ctx:Context):
    # TODO: send tooltip
    pass

  @cal.command(name='create')
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def cal_create(ctx:Context, channel:TextChannel, events_channel:TextChannel):
    calendar = db.Calendar(
      guild_id = ctx.guild.id,
      channel_id = channel.id,
      events_channel_id = events_channel.id
    )
    db.session.add(calendar)
    db.session.commit()

    embed = create_cal_embed(db)

    message = await channel.send(embed=embed)
    calendar.message_id = message.id
    db.session.commit()

    await ctx.send('Calendar created.')


  @cal.error
  @cal_create.error
  async def cal_error(ctx:Context, error:CommandError):
    if isinstance(error, commands.NoPrivateMessage):
      pass
    else:
      await ctx.send(error)