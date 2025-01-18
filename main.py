import discord
import sys
import os

from .config import EXTENSIONS, GUILD_ID
from .bot import run_bot

intents = discord.Intents.all()

bot = discord.Bot(intents=intents)

if not EXTENSIONS:
	print("No extensions to load.")

for extension in EXTENSIONS:
	try:
		bot.load_extension(extension)
		print(f'Successfully loaded extension: {extension}')

	except Exception as e:
		print(f'Failed to load extension {
				extension}: {e}', file=sys.stderr)

run_bot(bot)
