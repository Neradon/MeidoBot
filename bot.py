#!/usr/bin/env python3.6

import discord
import asyncio
import requests
import json
from vrchat_api import VRChatAPI
from discord.ext import commands

startup_extensions = [
"cogs.events",
"cogs.clever",
"cogs.reddit",
"cogs.BTC",
"cogs.husbando",
"cogs.update",
"cogs.userinfo",
"cogs.block_tenor",
"cogs.magic8ball",
"cogs.vrchat",
"cogs.voice"
]

client = discord.Client()

with open('token.json') as startup_data_file:
    startup_data = json.load(startup_data_file)
    startup_data_file.close()
    token = startup_data['tokens']['discord']['discord_token']
    prefix = startup_data['bot_settings']['prefix']
    vrcuser = startup_data['tokens']['vrchat']['username']
    vrcpw = startup_data['tokens']['vrchat']['password']
    cuttly = startup_data['tokens']['cuttly']['apiKey']

client = commands.Bot(command_prefix=(prefix),
                      pm_help=True,
                      case_insensitive=True,
                      owner_id=115895386606010376)

client.api = VRChatAPI(vrcuser, vrcpw)
client.api.authenticate()
client.cuttly = cuttly
client.friends = []
client.friendRequests  = []
client.acceptFriends = []
client.vrcCalls = []

client.remove_command('help')
'''
client.load_extension("jishaku")
'''

async def dontcrash():
    channels = client.get_all_channels()
    asyncio.sleep(50)

async def background_loop():
    await client.wait_until_ready()
    while True:

        worldIdToCheck = ""
        with open("worlds.json") as json_file:
            worlds = json.load(json_file)

        client.friends = client.api.getFriends()

        for f in client.friends:
            if f.location.worldId in worlds:
                f.worldName = worlds[f.location.worldId]
            else:
                f.worldName = "unknown"
                if f.location.worldId != "private":
                    print("unknown world "+f.location.worldId)
                    if worldIdToCheck == "":
                        worldIdToCheck = f.location.worldId
                        print("have to check world: "+worldIdToCheck)
                else:
                    f.worldName = "private"


        onlinemaid = str(len(client.friends))
        if len(client.friends) == 1:
            onlinemaid += " maid!"
        else:
            onlinemaid += " maids!"



        await client.change_presence(activity=discord.Activity(name=onlinemaid, type=3))
        print("updated maid count, now " + str(len(client.friends)))
        await asyncio.sleep(60)
        client.friendRequests = client.api.getFriendRequests()

        if worldIdToCheck != "":
            print("Waiting for Worldcheckcooldown...")
            await asyncio.sleep(60)
            print("Getting worldname: " + worldIdToCheck)
            worldName = client.api.getWorldById(worldIdToCheck).name
            with open("worlds.json") as json_file:
                worlds = json.load(json_file)
            worlds[worldIdToCheck] = worldName

            with open("worlds.json", "w") as outfile:
                json.dump(worlds, outfile)
        if len(client.acceptFriends) > 0:
            for f in client.friendRequests:
                if f.senderUsername in client.acceptFriends:
                    print("Accepting " + f.senderUsername + " with id: " + f.id)
                    await asyncio.sleep(60)
                    client.api.acceptFriendRequest(f.id)
                    client.acceptFriends.remove(f.senderUsername)
                    break





        await asyncio.sleep(60)

async def twitchlive():
    while True:
        await client.wait_until_ready()

        with open('twitch.json') as talk1:
            data1 = json.load(talk1)
            talk1.close()

        twitch_client_id = data1['token']['Twitch_Client-ID']
        streamers = data1['streamers']
        livemessage = None

        for streamer in streamers:

            if streamer == data1['streamers'][0]:
                live_notification = data1['discord']['live_notification']['streamer1']
                returndata_sendmsg = 'streamer1'
                returndata_msgid = 'disc_msg_id_str1'
            elif streamer == data1['streamers'][1]:
                live_notification = data1['discord']['live_notification']['streamer2']
                returndata_sendmsg = 'streamer2'
                returndata_msgid = 'disc_msg_id_str2'

            stream = requests.get("https://api.twitch.tv/helix/streams?user_id={0}".format(streamer), headers=twitch_client_id, timeout=None).json()

            if len(stream['data']) > 0:
                if live_notification == "notsendyet":
                    user = requests.get("https://api.twitch.tv/helix/users?id={0}".format(streamer),
                                        headers=twitch_client_id).json()
                    game = requests.get("https://api.twitch.tv/helix/games?id={0}".format(stream['data'][0]['game_id']),
                                        headers=twitch_client_id).json()

                    embed = discord.Embed(title=stream['data'][0]['title'], colour=discord.Colour(0x4b387a),
                                          url="https://twitch.tv/{}".format(stream['data'][0]['user_name']))
                    embed.set_image(url=stream['data'][0]['thumbnail_url'].format(width='1920', height='1080'))
                    embed.set_thumbnail(url=game['data'][0]['box_art_url'].format(width='272', height='380'))
                    embed.set_author(name=stream['data'][0]['user_name'],
                                     icon_url=user['data'][0]['profile_image_url'])
                    embed.set_footer(text="Twitch Livestream",
                                     icon_url="https://pngimg.com/uploads/twitch/twitch_PNG22.png")

                    embed.add_field(name="Game:", value=game['data'][0]['name'], inline=True)
                    embed.add_field(name="Viewers", value=stream['data'][0]['viewer_count'], inline=True)

                    channel = client.get_channel(int(data1['discord']['discord_channel']))
                    livemessage = await channel.send(embed=embed)

                    with open('twitch.json', 'w') as returndata:
                        data1['discord']['live_notification']["{}".format(returndata_sendmsg)] = "alreadysend"
                        data1['discord']['live_notification']["{}".format(returndata_msgid)] = "{0}".format(livemessage.id)
                        json.dump(data1, returndata)
                        talk1.close()

            else:
                with open('twitch.json', 'w') as returndata:
                    data1['discord']['live_notification']["{}".format(returndata_sendmsg)] = "notsendyet"
                    json.dump(data1, returndata)
                    talk1.close()

                if livemessage is not None:
                    await livemessage.delete()

        await asyncio.sleep(900)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
client.loop.create_task(dontcrash())
client.loop.create_task(background_loop())
client.loop.create_task(twitchlive())
client.run(token, bot=True, reconnect=True)
