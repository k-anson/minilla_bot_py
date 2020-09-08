from discord.ext.commands import Bot
from sqlalchemy.orm import Session
from discord.ext.commands import Context

def create_cal_commands(config:dict, client:Bot, db:Session):
  @client.group(invoke_without_command=True)
  async def cal(ctx:Context):
    pass

  @cal.command()
  async def create(ctx:Context):
    pass