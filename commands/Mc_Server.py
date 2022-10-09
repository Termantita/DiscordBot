from discord import Embed, Color
from discord.ext import commands as client
from requests import get
from datetime import datetime


class McCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='server')
    async def minecraft_server(self, ctx, *, arg):
        # try:
        server = get(f'https://api.mcsrvstat.us/2/{arg}')
        data = server.json()

        embed = Embed(title='Minecraft server', color=Color.blue())
        embed.add_field(name='Server IP/Domain', value=str(data['hostname']) + ' (' + str(
            data['ip']) + ':' + str(data['port']) + ')', inline=False)
        try:
            embed.add_field(name='Online', value='🟢')
            embed.add_field(name='Players 👥', value=str(
                data['players']['online']) + ' / ' + str(data['players']['max']), inline=False)
            embed.add_field(name='MOTD', value=str(
                data['motd']['clean'][0]), inline=False)
            embed.add_field(name='Server version', value=str(data['version']))
        except Exception as e:
            print(e)
            embed = Embed(title='Minecraft server',
                          color=Color.blue())
            embed.add_field(name='Online', value='🔴')
        embed.set_thumbnail(url=f'https://api.mcsrvstat.us/icon/{arg}')
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text='Discord Bot By Terma')

        await ctx.send(embed=embed)