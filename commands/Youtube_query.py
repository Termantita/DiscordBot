from discord.ext import commands as client
from re import findall
from asyncio import TimeoutError
from bs4 import BeautifulSoup
from requests import get


class QYoutubeCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='youtube')
    async def Youtube_Query(self, ctx, *, search):
        watch_string = 'https://www.youtube.com/'
        query_string = f'https://www.youtube.com/results?search_query={search}'
        req = get(query_string)
        content = BeautifulSoup(req.text, 'lxml')
        search_results = findall(r'watch\?v=.{11}', str(content.select('script')))
        search_results = set(search_results)
        search_results = list(search_results)
        if search_results is None:
            await ctx.send('No se encontró ningun resultado.')
        else:
            await ctx.send(watch_string + search_results[0])
            await ctx.send('Escriba next para obtener la siguiente busqueda')
            for i in range(1, len(search_results)):
                try:
                    msg = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author,
                                                  timeout=10)
                    if msg and msg.content == 'next':
                        await ctx.send(watch_string + search_results[i])
                        await ctx.send('Escriba next para obtener la siguiente busqueda')
                except TimeoutError:
                    print('Query finished.')
                    await ctx.send('Busqueda terminada.')
                    break

    @Youtube_Query.error
    async def Youtube_Query_error(self, ctx, error):
        if isinstance(error, client.MissingRequiredArgument):
            await ctx.send('Falta el argumento de busqueda.')
        else:
            print(error)
