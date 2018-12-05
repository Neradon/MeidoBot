#!/usr/bin/env python3

import discord
import asyncio
import requests
import json
import urllib.parse
from discord.ext import commands

startup_extensions = [
"cogs.events",
"cogs.no_erp",
"cogs.clever",
"cogs.reddit",
"cogs.BTC",
"cogs.husbando",
"cogs.update"
]

client = discord.Client()

with open('token.json') as token_file:
    data = json.load(token_file)
token = data['tokens']['discord_token']
prefix = data['prefix']

client = commands.Bot(command_prefix=(prefix),
                    pm_help=True,
                    case_insensitive=True,
                    owner_id=115895386606010376)

client.remove_command('help')
client.load_extension("jishaku")

async def background_loop():
    while True:
        await client.wait_until_ready()
        online = []
        x = client.get_all_members()
        for member in x:
            if member.status == discord.Status.online:
                online.append(member)
            elif member.status == discord.Status.idle:
                online.append(member)
            elif member.status == discord.Status.dnd:
                online.append(member)
        onlinemaid = "{0} maids!".format(str(len(set(online)) -1))

        await client.change_presence(activity=discord.Activity(name=onlinemaid, type=3))
        print("updated maid count, now " + str(len(set(online)) -1))
        await asyncio.sleep(420)

async def twitchlive():
    while True:
        await client.wait_until_ready()

        with open('token.json') as talk1:
            data1 = json.load(talk1)
            talk1.close()

        with open('twitch.json') as talk:
            data = json.load(talk)
            talk.close()


        streamer = data1['streamer']
        livemessage = None

        stream = requests.get("https://api.twitch.tv/helix/streams?user_login={0}".format(streamer), headers=data).json()

        if len(stream['data']) > 0:
            if data1['live_noti'] == "notsendyet":
                user = requests.get("https://api.twitch.tv/helix/users?login={0}".format(streamer), headers=data).json()
                game = requests.get("https://api.twitch.tv/helix/games?id={0}".format(stream['data'][0]['game_id']), headers=data).json()

                embed = discord.Embed(title=stream['data'][0]['title'], colour=discord.Colour(0x4b387a), url="https://twitch.tv/{}".format(streamer))
                embed.set_image(url=stream['data'][0]['thumbnail_url'].format(width='1920', height='1080'))
                embed.set_thumbnail(url=game['data'][0]['box_art_url'].format(width='272', height='380'))
                embed.set_author(name=stream['data'][0]['user_name'],
                                 icon_url=user['data'][0]['profile_image_url'])
                embed.set_footer(text="Twitch Livestream",
                                 icon_url="https://pngimg.com/uploads/twitch/twitch_PNG22.png")

                embed.add_field(name="Game:", value=game['data'][0]['name'], inline=True)
                embed.add_field(name="Viewers", value=stream['data'][0]['viewer_count'], inline=True)

                channel = client.get_channel(int(data1['discord_twitch_channel']))
                livemessage = await channel.send(embed=embed)

                with open('token.json', 'w') as talk1:
                    
                    data1['live_noti'] = "alreadysend"
                    data1['discord_message_id'] = "{0}".format(livemessage.id)
                    json.dump(data1, talk1)
                    talk1.close()

        else:
            with open('token.json', 'w') as talk1:

                data1['live_noti'] = "notsendyet"
                json.dump(data1, talk1)
                talk1.close()

            if livemessage is not None:
                await livemessage.delete()

        await asyncio.sleep(420)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.loop.create_task(background_loop())
client.loop.create_task(twitchlive())
client.run(token, bot=True, reconnect=True)
