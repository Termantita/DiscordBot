from discord import Embed, Color
from discord.ext import commands as client
from random import randint


class RpsCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='game')
    async def r_p_s(self, ctx, *, arg):
        def get_IA_Choice():
            opt = randint(1, 3)
            elements = {1: 'piedra', 2: 'papel', 3: 'tijera'}
            IA_Option = elements[opt]
            return IA_Option

        def get_Result(user, ia):
            if user == ia:
                return 'Empate!'
            elif user == 'roca' and ia == 'tijera':
                return 'Ganaste!'
            elif user == 'tijera' and ia == 'papel':
                return 'Ganaste!'
            elif user == 'papel' and ia == 'piedra':
                return 'Ganaste!'
            else:
                return 'Perdiste!'

        IA_Choice = get_IA_Choice()
        while True:
            user_Choice = arg.lower()
            if user_Choice in ['piedra', 'papel', 'tijera']:
                break
            else:
                await ctx.send('Opción inválida!')
                raise ValueError('Opción inválida')

        result = get_Result(IA_Choice, user_Choice)
        emojis = {'piedra': '✊🏻', 'papel': '✋🏻', 'tijera': '✌🏻'}
        urls = {'Empate!': 'https://media3.giphy.com/media/3ohzdGnD5vAud1NCZW/giphy.gif',
                'Ganaste!': 'https://c.tenor.com/GkjzkpREwhkAAAAC/winner-xirtus.gif',
                'Perdiste!': 'https://33.media.tumblr.com/57210f49c08bd1d5d79bea0a51d4983a/tumblr_ngfbelEq3v1shxdt9o1_500.gif'}
        embed = Embed(title=result, color=Color.blue())
        embed.add_field(name='Elección de la IA', value=emojis[IA_Choice], inline=True)
        embed.add_field(name='Tu elección', value=emojis[user_Choice], inline=True)
        embed.set_image(url=urls[result])

        await ctx.send(embed=embed)

    @r_p_s.error
    async def r_p_s_error(self, ctx, error):
        if isinstance(error, client.MissingRequiredArgument):
            await ctx.send('No se ingreso la opción a jugar.')
        else:
            print(error)