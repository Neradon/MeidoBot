import discord
import asyncio
import json
from discord.ext import commands

startup_extensions = [
"cogs.events",
"cogs.no_erp",
"cogs.clever"
]

client = discord.Client()

with open('token.json') as token_file:
	data = json.load(token_file)
token = data['token']


client = commands.Bot(command_prefix=('#','maid.'),
					pm_help=True,
					case_insensitive=True,
					owner_id=115895386606010376,
					activity=discord.Game("with Maids"))

client.remove_command('help')
client.load_extension("jishaku")

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			client.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))


client.run(token, bot=True, reconnect=True)
