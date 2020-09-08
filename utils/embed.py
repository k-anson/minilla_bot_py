from discord import Embed, Color
from datetime import datetime, timedelta

from database import Database

def create_cal_embed(db:Database) -> Embed:
  embed = Embed(
    color = Color.blue()
  )

  # Loop over next 21 days
  date:datetime = datetime.today()
  for i in range(21):
    embed.add_field(name=date.strftime('%A, %B %d'), value='No Events', inline=True)
    date += timedelta(days=1)

  # Add 'Future Events' field

  return embed