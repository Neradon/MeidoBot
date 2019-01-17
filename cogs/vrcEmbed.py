import requests
import _asyncio
import json
import discord
from discord.ext import commands

class vrcEmbed:

    def __init__(self, client):
        self.client = client

    global i
    i = 1

    @commands.command()
    async def vrce(self, ctx, *, arg1):

        global arg2
        global s
        global userinfo
        global embeddedmessage
        global messagecon


        arg2 = arg1
        s = requests.session()
        messagecon = ctx.message.author

        request = s.get("https://www.vrchat.net/api/1/config").json()
        request2 = s.get("https://www.vrchat.net/api/1/auth/user?apiKey={0}".format(request['apiKey']),
                         auth=('LSparky', 'aeiou1234')).json()
        search = s.get("https://www.vrchat.net/api/1/users?search={}".format(arg1)).json()

        userinfo = s.get("https://www.vrchat.net/api/1/users/{}".format(search[i]['id'])).json()

        embed = discord.Embed(title="Name: {}".format(userinfo['displayName']), colour=discord.Colour(0x99aa5),
                              url="https://www.vrchat.net/home/user/{0}".format(userinfo['id']))

        embed.set_thumbnail(url="{}".format(userinfo['currentAvatarImageUrl']))
        embed.set_author(name="VRC API", icon_url="https://api.vrchat.cloud/public/media/logo@2x.png")
        embed.set_footer(text="Requested by: {}".format(messagecon.name),
                         icon_url=messagecon.avatar_url)

        embeddedmessage = await ctx.send(content="Showing API Data:", embed=embed)

        await embeddedmessage.add_reaction("◀")
        await embeddedmessage.add_reaction("▶")

    async def on_raw_reaction_add(self, payload):
        global i
        if payload.message_id == embeddedmessage.id:
            if payload.user_id == self.client.user.id:
                return
            else:
                if i == 0:
                    await embeddedmessage.clear_reactions()
                    await embeddedmessage.add_reaction("▶")
                else:
                    await embeddedmessage.clear_reactions()
                    await embeddedmessage.add_reaction("◀")
                    await embeddedmessage.add_reaction("▶")
                if payload.emoji.name == "◀":
                    i = i-1

                    search = s.get("https://www.vrchat.net/api/1/users?search={}".format(arg2)).json()

                    userinfo = s.get("https://www.vrchat.net/api/1/users/{}".format(search[i]['id'])).json()

                    embed1 = discord.Embed(title="Name: {}".format(userinfo['displayName']),
                                           colour=discord.Colour(0x99aa5),
                                           url="https://www.vrchat.net/home/user/{0}".format(userinfo['id']))

                    embed1.set_thumbnail(url="{}".format(userinfo['currentAvatarImageUrl']))
                    embed1.set_author(name="VRC API", icon_url="https://api.vrchat.cloud/public/media/logo@2x.png")
                    embed1.set_footer(text="Requested by: {}".format(messagecon.name),
                                      icon_url=messagecon.avatar_url)

                    await embeddedmessage.edit(content="Number is: {}".format(i), embed=embed1)

                elif payload.emoji.name == "▶":
                    i = i+1

                    search = s.get("https://www.vrchat.net/api/1/users?search={}".format(arg2)).json()

                    userinfo = s.get("https://www.vrchat.net/api/1/users/{}".format(search[i]['id'])).json()

                    embed1 = discord.Embed(title="Name: {}".format(userinfo['displayName']),
                                          colour=discord.Colour(0x99aa5),
                                          url="https://www.vrchat.net/home/user/{0}".format(userinfo['id']))

                    embed1.set_thumbnail(url="{}".format(userinfo['currentAvatarImageUrl']))
                    embed1.set_author(name="VRC API", icon_url="https://api.vrchat.cloud/public/media/logo@2x.png")
                    embed1.set_footer(text="Requested by: {}".format(messagecon.name),
                                     icon_url=messagecon.avatar_url)

                    await embeddedmessage.edit(content="Number is: {}".format(i), embed=embed1)


def setup(client):
    client.add_cog(vrcEmbed(client))