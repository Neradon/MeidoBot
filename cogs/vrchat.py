import discord
import requests
import json
from discord.ext import commands
from vrchat_api import VRChatAPI
from requests.auth import HTTPBasicAuth
from mcstatus import MinecraftServer

class vrchat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def online(self, ctx):
        s = "**[Gamers online]**\n"
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

        if s == "**[Gamers online]**\n":
            s = "No Gamers online <:maidHands:463442634728538122>"
        await ctx.send(s)

    @commands.command()
    async def offline(self, ctx):
        s = "Unknown~"
        await ctx.send(s)

    @commands.command()
    async def onlineinminecraft(self, ctx):
        s = ""
        try:
            server = MinecraftServer.lookup("mc.battlemaids.net")
            status = server.status()
            self.client.mcfriends = status.players.online
            s = "{0} players online: ".format(self.client.mcfriends)+"\n"
            for p in status.players.sample:
                s += p.name+"\n"
        except:
            s = "0 players online"
            self.client.mcfriends = 0
        await ctx.send(s)

    @commands.command()
    async def addFriend(self, ctx, name):
        if name != "":
            if name in self.client.acceptFriends:
                s = "You are already in my list!"
            else:
                s = "I will accept your friendrequest ^.^"
                self.client.acceptFriends.append(name)
        else:
            s = "Syntax is $addFriend YourVRChatName"
        await ctx.send(s)

    @commands.command()
    async def listFriendRequests(self, ctx):
        s = "**[Friendrequests]**\n"
        for f in self.client.friendRequests:
            s += f.senderUsername+"\n"

        if len(self.client.acceptFriends) > 0:
            s += "\n**[On my auto accept list]**\n"
            for f in self.client.acceptFriends:
                s += f+"\n"

        if s == "**[Friendrequests]**\n":
            s = "No friendrequests"
        await ctx.send(s)

    @commands.command()
    async def name(self, ctx):
        s = "My VRChat name is **Maidobot** (∪ ◡ ∪)\n"
        s += "I'm always happy to meet new people (✿◠‿◠)"
        await ctx.send(s)

    @commands.command()
    async def help(self, ctx):
        s = "**[VRChat Commands]**\n"
        s += "$online - List all online friends of Meido\n"
        s += "$offline - List all offline friends of Meido\n"
        s += "$addFriend \"YourVRChatName\" - Adds your name to the auto accept list\n"
        s += "$listFriendRequests - Lists all friendrequests Meido has at the moment\n"
        s += "$name - Shows Meidos VRChat name\n"
        await ctx.send(s)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def sendmessage(self,ctx,user,message):
        s = "Sent message!"
        with open("users.json") as json_file:
            users = json.load(json_file)
        if str(user).lower() in users:
            self.client.api.sendMessage(users[str(user).lower()],message)
        else:
            s = "No user found for: "+user+" :("
        await ctx.send(s)

def setup(client):
    client.add_cog(vrchat(client))