import json
import discord 
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('AL_TOKEN')

class player_stats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['ps'])
    async def player_stats(self, ctx, arg1, arg2):
        response = requests.get('https://api.mozambiquehe.re/bridge?version=5&platform=PC&player={}&auth={}' .format(arg1, TOKEN))
        data = response.json()
        #print(json.dumps(data, sort_keys=False, indent=4))
        legend_stats = data['legends']['all'][arg2]['data']
        await ctx.send(legend_stats)


def setup(client):
    client.add_cog(player_stats(client))