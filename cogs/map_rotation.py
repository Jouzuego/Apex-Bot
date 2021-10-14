import discord
from discord.ext import commands
import requests

class map_rotation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['map rotation', 'mr'])
    async def map_rotation(self, ctx):
        response = requests.get('https://api.mozambiquehe.re/maprotation?lang=en-us&auth=ZzI6eVvodK8CuURB0Okx')
        data = response.json()
        current_map = data['current']['map']
        current_map_timer = data['current']['remainingTimer']
        next_map = data['next']['map']
        next_map_duration = data['next']['DurationInMinutes']
        
        await ctx.send('The current map is: {}. Time left on current map: {}. The next map is: {}. Time on next map will be {} min '.format(current_map, current_map_timer, next_map, next_map_duration))
        

        

    
 
def setup(client):
        client.add_cog(map_rotation(client))       
        
