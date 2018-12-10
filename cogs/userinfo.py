import discord
import datetime
from discord.ext import commands

class userinfo:

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['user', 'info', 'userstats'])
    async def userinfo(self, ctx, userName: discord.Member=None):
        if not userName:
            roles = ""
            for role in ctx.message.author.roles:
                roles = roles + ("{}\n").format(role)
            embed=discord.Embed(color=ctx.message.author.color, timestamp=datetime.datetime.now())
            embed.set_image(url= ctx.message.author.avatar_url)
            embed.add_field(name="Name: ", value=ctx.message.author.name, inline=True)
            embed.add_field(name="Nickname: ", value=ctx.message.author.nick, inline=True)
            embed.add_field(name="Status: ", value=ctx.message.author.status, inline=True)
            embed.add_field(name="Roles: ", value=roles, inline=True)
            embed.add_field(name="Created account: ", value=ctx.message.author.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
            embed.add_field(name="Joined server: ", value=ctx.message.author.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
            embed.add_field(name="Avatar URL: ", value=ctx.message.author.avatar_url, inline=True)
            embed.set_footer(text="User ID: " + str(ctx.message.author.id))
            await ctx.send(content="Here you go " + ctx.message.author.mention + "!", embed=embed)
        else:
            roles = ""
            for role in userName.roles:
                roles = roles + ("{}\n").format(role)
            embed=discord.Embed(color=userName.color, timestamp=datetime.datetime.now())
            embed.set_image(url= userName.avatar_url)
            embed.add_field(name="Name: ", value=userName.name, inline=True)
            embed.add_field(name="Nickname: ", value=userName.nick, inline=True)
            embed.add_field(name="Status: ", value=userName.status, inline=True)
            embed.add_field(name="Roles: ", value=roles, inline=True)
            embed.add_field(name="Created account: ", value=userName.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
            embed.add_field(name="Joined server: ", value=userName.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
            embed.add_field(name="Avatar URL: ", value=userName.avatar_url, inline=True)
            embed.set_footer(text="User ID: " + str(userName.id))
            await ctx.send(content="Here you go " + ctx.message.author.mention + "!", embed=embed)

def setup(client):
    client.add_cog(userinfo(client))