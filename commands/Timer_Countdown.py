from discord.ext import commands as client
from asyncio import sleep


class TimerCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='timer')
    async def timer(self, ctx, *, arg):
        seconds, unit = arg.split(' ')
        seconds = int(seconds)

        if seconds == 0:
            await ctx.send('No existe un contador de 0 segundos.')
            raise ValueError('No existe un contador de 0 segundos.')
        if unit == 's':
            pass
        elif unit == 'm':
            seconds *= 60
        elif unit == 'h':
            await ctx.send('No se puede hacer un contador de una hora o más.')
            raise TimeoutError('No se puede hacer un contador de una hora o más.')
        else:
            await ctx.send('La unidad ingresada no es válida.')
            raise ValueError('La unidad ingresada no es válida')

        if seconds >= 1800:
            await ctx.send('El contador es muy largo.')
            raise TimeoutError('El contador es muy largo.')
        else:
            await ctx.send('Comenzando a contar...')
            for s in range(seconds):
                await sleep(1)
                print(s, sep='-', flush=True, end='')
            else:
                await ctx.send(f'Contador terminado. ({str(seconds)}s)')

    @timer.error
    async def timer_error(self, ctx, error):
        if isinstance(error, client.MissingRequiredArgument):
            await ctx.send('Falta el argumento de tiempo.')
        else:
            print(error)