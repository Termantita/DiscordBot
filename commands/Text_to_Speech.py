from discord.ext import commands as client


class StartCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='start')
    async def Console_to_Discord(self, ctx):
        x = ''
        while not x == 'exit':
            x = input('Ingrese: ')
            await ctx.send(x)
        else:
            print('Fin del callback.')