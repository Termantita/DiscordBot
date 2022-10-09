from discord import Embed, Color
from discord.ext import commands as client
from requests import get
from socket import socket, AF_INET, SOCK_STREAM, setdefaulttimeout, error


class PortscanCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='scan')
    async def ip_scan(self, ctx, *, arg):
        try:
            server = get(f'https://api.mcsrvstat.us/2/{arg}')
            data = server.json()

            ip = str(data['ip'])
            for port in range(25565, 65535):
                s = socket(AF_INET, SOCK_STREAM)
                setdefaulttimeout(0.5)

                result = s.connect_ex((ip, port))
                if result == 0:
                    embed = Embed(title='Open ports',
                                  color=Color.purple())
                    embed.add_field(
                        name='Ports', value='''[*] Puerto {} está abierto'''.format(port))

                    await ctx.send(embed=embed)
                s.close()

        except error:
            ctx.send('Host is not responding...')

    @ip_scan.error
    async def ip_scan_error(self, ctx, error):
        if isinstance(error, client.MissingRequiredArgument):
            await ctx.send('No se ingreso el Hostname/IP a escanear.')
        else:
            print(error)