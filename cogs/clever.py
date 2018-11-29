#script scuffed by bahka, fixed up by Sparky

import discord
from discord.ext import commands
from cleverwrap import CleverWrap

cw = CleverWrap('CCCrw8x-1eic8qi3Q-mrPc1Sutw')

class clever:
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def clever(self, ctx):
		param = ctx.message.content[2:]
		if len(param) > 2:

			await ctx.channel.send(cw.say(param))
		else:
			await ctx.channel.send('use !m <message>')

def setup(client):
	client.add_cog(clever(client))
