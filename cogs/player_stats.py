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
    async def player_stats(self, ctx, arg1):
        response = requests.get('https://api.mozambiquehe.re/bridge?version=5&platform=PC&player={}&auth={}' .format(arg1, TOKEN))
        data = response.json()
        #print(json.dumps(data, sort_keys=False, indent=4))
        print(json.dumps(data['total'], sort_keys=False, indent=4))
        player_kills = data['total']['kills']['value']
        player_kd = data['total']['kd']['value']
        player_rank_name = data['global']['rank']['rankName']
        player_rank_div = data['global']['rank']['rankDiv']
        
        await ctx.send("Total kills: {}.  KD: {}. rank: {} {}" .format(player_kills, player_kd, player_rank_name, player_rank_div))

    @commands.command(aliases = ['ls'])
    async def legend_stats(self, ctx, arg1, arg2):
        response = requests.get('https://api.mozambiquehe.re/bridge?version=5&platform=PC&player={}&auth={}' .format(arg1, TOKEN))
        data = response.json()
        print(json.dumps(data['legends']['all'][arg2], sort_keys=False, indent=4))
        legend_icon = data['legends']['all'][arg2]['ImgAssets']['icon']
        await ctx.send("{}" .format(legend_icon))
        for tracker in data["legends"]["all"][arg2]["data"]:
            legend_tracker_name = tracker['name']
            legend_tracker_value =tracker['value']
            await ctx.send("{}: {}" .format(legend_tracker_name, legend_tracker_value))

    



def setup(client):
    client.add_cog(player_stats(client))