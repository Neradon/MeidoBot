import discord
import requests
from discord.ext import commands

class BTC:
	def __init__(self, client):
		self.client = client
		
	@commands.command()
	async def BTC(self, ctx):
		data = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json').json()
		cur = data['bpi']['USD']['rate']
		await ctx.send(str(cur)+" USD")

def setup(client):
	client.add_cog(BTC(client))
	
