import discord
from discord.ext import commands as client
from string import ascii_lowercase
from random import randint


class GeneratorCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='gen')
    async def Random_Key(self, ctx, *, arg):
        arg = arg.lower()
        length, method = arg.split(' ')

        def Gen_key(key_length: int, method):
            key, serial = '', ''
            symbols = {27: '~', 28: ':', 29: "'", 30: '+', 31: '[', 32: '\\', 33: '@', 34: '^', 35: '{', 36: '%',
                       37: '(', 38: '-', 39: '"', 40: '*', 41: '|', 42: ',', 43: '&', 44: '<', 45: '`', 46: '}',
                       47: '.', 48: '_', 49: '=', 50: ']', 51: '!', 52: '>', 53: ';', 54: '?', 55: '#', 56: '$',
                       57: ')', 58: '/'}
            alphabet = dict(enumerate(ascii_lowercase, 1))

            if method == 'key':
                for i in range(key_length):
                    key += str(randint(0, 9))
                return key
            elif method == 'serial':
                for i in range(key_length):
                    r = randint(0, 2)
                    if r == 0:
                        serial += str(alphabet[randint(1, 26)])
                    elif r == 1:
                        serial += str(alphabet[randint(1, 26)].upper())
                    elif r == 2:
                        serial += str(randint(0, 9))
                return serial
            elif method == 'serial2':
                alphabet.update(symbols)
                for i in range(key_length):
                    r = randint(0, 2)
                    if r == 0:
                        serial += str(alphabet[randint(1, 58)])
                    elif r == 1:
                        serial += str(alphabet[randint(1, 58)].upper())
                    elif r == 2:
                        serial += str(randint(0, 9))
                return serial
            else:
                return 'Invalid method.'

        gen = Gen_key(int(length), method)
        if len(gen) > 40:
            await ctx.send('La generación es muy larga. Maximo 40')
            raise Exception('Key muy larga.')
        else:

            embed = discord.Embed(color=discord.Color.red())
            embed.add_field(name='Key', value=gen)
            print(f'Generated key: {gen}')
            await ctx.send(embed=embed)
