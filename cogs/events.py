import discord
from discord.ext import commands

class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	async def on_ready(self):
		print("logged in as {0.user.name}\n ID: {0.user.id}".format(self.client))

def setup(client):
    client.add_cog(events(client))
