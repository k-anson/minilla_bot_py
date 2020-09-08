# import discord
from discord.ext import commands
from discord.ext.commands import Context

from config import config
from database import create_db_session
from commands.cal_commands import create_cal_commands

client = commands.Bot(command_prefix='!')
db = create_db_session(config)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

create_cal_commands(config, client, db)

client.run(config['CLIENT_TOKEN'])