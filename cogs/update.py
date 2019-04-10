import json
import requests
from discord.ext import commands

class Update(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def update(self, ctx):

        with open('twitch.json') as talk1:
            data1 = json.load(talk1)
            talk1.close()

        streamers = data1['streamers']
        twitch_client_id = data1['token']['Twitch_Client-ID']

        for streamer in streamers:

            stream = requests.get("https://api.twitch.tv/helix/streams?user_id={0}".format(streamer), headers=twitch_client_id).json()

            if streamer == data1['streamers'][0]:
                live_notification = data1['discord']['live_notification']['streamer1']
                returndata_msgid = 'disc_msg_id_str1'
                print("Streamer 1")
            elif streamer == data1['streamers'][1]:
                live_notification = data1['discord']['live_notification']['streamer2']
                returndata_msgid = 'disc_msg_id_str2'
                print("Streamer 1")

            if live_notification == "alreadysend":
                print("i am here now")
                channel = self.client.get_channel(int(data1['discord']['discord_channel']))
                livemessage = await channel.get_message(int(data1['discord']['live_notification']["{}".format(returndata_msgid)]))
                print(livemessage)
                await livemessage.delete()

        await ctx.send("Updating bot and restarting...")
        await self.client.close()

def setup(client):
    client.add_cog(Update(client))
