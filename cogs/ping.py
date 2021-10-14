import discord
from discord.ext import commands 

class ping(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    

    # commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')



def setup(client):
    client.add_cog(ping(client))
