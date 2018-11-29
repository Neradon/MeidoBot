#script scuffed by bahka, fixed up by Sparky

import discord
import json
from discord.ext import commands
from cleverwrap import CleverWrap

with open('token.json') as token_file:
	data = json.load(token_file)
clevertoken = data['clevertoken']

cw = CleverWrap(clevertoken)

class clever:
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def clever(self, ctx):
		param = ctx.message.content
		await ctx.send(cw.say(param))

	@commands.command()
	async def clever_reset(self, ctx):
		cw.reset()
		await ctx.send("Reset conversation!")

def setup(client):
	client.add_cog(clever(client))
