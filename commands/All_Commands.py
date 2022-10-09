import discord
from discord.ext import commands as client


class CommandsCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='commands')
    async def get_cmds(self, ctx):
        result = ''
        bot_commands = ctx.bot.all_commands.keys()
        for command in bot_commands:
            result += '-' + command
        else:
            await ctx.send(result)
