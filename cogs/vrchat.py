import discord
import requests
from discord.ext import commands
from vrchat_api import VRChatAPI
from requests.auth import HTTPBasicAuth


class vrchat:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def online(self, ctx):
        s = "**[Battlemaids online]**\n"
        friends = self.client.friends
        for f in friends:
            if f.location.worldId != "private":
                url = requests.get(
                    "https://cutt.ly/api/api.php?key=" + self.client.cuttly + "&short=+http://neradonien.de/redirect.php?world=" + f.location.worldId + ":" + f.location.instanceId,
                )
                s += f.username+" - "+f.worldName+" -> "+str(url)
            elif f.location.worldId == "private":
                s += f.username + " - " + f.worldName + " <a:HNNNNG:470332847190966319>"
            else:
                s += f.username + " - " + f.worldName

        if s == "**[Battlemaids online]**\n":
            s = "No Battlemaid online <:maidHands:463442634728538122>"
        await ctx.send(s)

    @commands.command()
    async def acceptFriends(self, ctx):
        '''
        s = "Accepted friends:\n"
        friends = api.getFriendRequests()
        for f in friends:
            s += f.senderUsername + "\n"
            api.acceptFriendRequest(f.id)
        if s == "Accepted friends:\n":
            s = "No friendrequests"
        '''
        s = "Coming soon..."
        await ctx.send(s)


def setup(client):
    client.add_cog(vrchat(client))