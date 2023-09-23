# pylint: disable-all
import time
import discord
from dotenv import dotenv_values

class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(config["CHANNEL_ID"]))
        while True:
            await channel.send(config["MESSAGE"])
            time.sleep(60)

client = MyClient()
config = dotenv_values(".env")
client.run(config["DISCORD_TOKEN"])
