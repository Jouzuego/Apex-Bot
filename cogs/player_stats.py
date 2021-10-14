import discord 
from discord.ext import commands
import requests

class player_stats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def player_stats(self, ctx):
        response = requests.get('https://api.mozambiquehe.re/bridge?version=5&platform=PC&player=Jozuego&auth=ZzI6eVvodK8CuURB0Okx')
        data = response.json()


def setup(client):
    client.add_cog(player_stats(client))