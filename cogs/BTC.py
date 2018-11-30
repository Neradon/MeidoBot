import json
import discord
import requests
from discord.ext import commands

urll = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'

class BTC:
	def __init__(self, client):
		self.client = client
		
	@commands.command()
	async def BTC(self, ctx):
		data = requests.get(urll).json()
		cur = data['bpi']['USD']['rate']
		msg = str(cur)+" USD"
		await ctx.send(msg)

def setup(client):
	client.add_cog(BTC(client))
	
