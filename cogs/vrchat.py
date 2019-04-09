import discord
import requests
import json
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
            s += f.displayName + " - "
            if f.location.worldId == "private":
                s += f.worldName + " <a:HNNNNG:470332847190966319>"
            elif "~hidden" in f.location.instanceId:
                s += f.worldName + " -> friends only"
            else:
                ret = requests.get(
                    "https://cutt.ly/api/api.php?key=" + self.client.cuttly + "&short=http://neradonien.de/redirect.php?world=" + f.location.worldId + ":" + f.location.instanceId,
                )
                data = json.loads(ret.text)
                if data["url"]["status"] == 7:
                    s += f.worldName+" -> " + str(data["url"]["shortLink"])
                else:
                    s += f.worldName + " -> unknown"
            s += "\n"

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