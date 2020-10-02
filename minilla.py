# import discord
from discord.ext import commands

from config import config
from database import Database
from commands.cal_commands import create_cal_commands
from commands.calevent_commands import create_calevent_commands

client = commands.Bot(command_prefix='!')
db = Database(config)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

create_cal_commands(config, client, db)
create_calevent_commands(config, client, db)

client.run(config['CLIENT_TOKEN'])