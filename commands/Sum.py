from discord.ext import commands as client


class SumCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='sum')
    async def add(self, ctx, *, arg):
        n1, n2 = arg.split('+')
        await ctx.send(int(n1) + int(n2))