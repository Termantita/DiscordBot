import discord
from discord.ext import commands as client


class TalktoDMCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='md')
    async def talk_to_dm(self, ctx):
        dm = await ctx.message.author.create_dm()
        await dm.send('Hola 😋')
        await ctx.send('@everyone')
