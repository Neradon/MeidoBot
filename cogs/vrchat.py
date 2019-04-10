import discord
import requests
import json
from discord.ext import commands
from vrchat_api import VRChatAPI
from requests.auth import HTTPBasicAuth


class vrchat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def online(self, ctx):
        s = "**[Battlemaids online]**\n"
        friends = self.client.friends
        worldShortcuts = {}
        for f in friends:
            s += f.displayName + " - "
            if f.location.worldId == "private":
                s += f.worldName + " <a:HNNNNG:470332847190966319>"
            elif "~hidden" in f.location.instanceId:
                s += f.worldName + " -> friends only"
            else:
                url = f.location.worldId + ":" + f.location.instanceId
                if url in worldShortcuts:
                    s += f.worldName + " -> "+worldShortcuts[url]
                else:
                    ret = requests.get(
                        "https://cutt.ly/api/api.php?key=" + self.client.cuttly + "&short=http://neradonien.de/redirect.php?world=" + url,
                    )
                    data = json.loads(ret.text)
                    if data["url"]["status"] == 7:
                        s += f.worldName + " -> " + str(data["url"]["shortLink"])
                        worldShortcuts[url] = str(data["url"]["shortLink"])
                    else:
                        s += f.worldName + " -> unknown"
                        worldShortcuts[url] = "unknown"


            s += "\n"

        if s == "**[Battlemaids online]**\n":
            s = "No Battlemaid online <:maidHands:463442634728538122>"
        await ctx.send(s)

    @commands.command()
    async def addFriend(self, ctx, name):

        if name != "":
            if name in self.client.acceptFriends:
                s = "You are already in my list!"
            else:
                s = "Added you to my list!"
                self.client.acceptFriends.append(name)
        else:
            s = "Syntax is $addFriend YourVRChatName"
        await ctx.send(s)


def setup(client):
    client.add_cog(vrchat(client))