from discord.ext import commands as client


class LoopCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='loop')
    async def loop(self, ctx, *, arg):
        if not int(arg) > 10:
            for i in range(int(arg)):
                await ctx.send(i + 1)
        else:
            await ctx.send('No te pases.')

    @loop.error
    async def loop_error(self, ctx, error):
        if isinstance(error, client.MissingRequiredArgument):
            await ctx.send('Falta el argumento de tiempo.')
        else:
            print(error)