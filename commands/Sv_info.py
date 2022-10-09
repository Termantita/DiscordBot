from discord.ext import commands as client


class SvInfoCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot


@client.command(name='info')
async def display_guild_about(ctx):
    await ctx.send(
        f'''Información pedida por *{ctx.message.author}*,
en el canal **{ctx.message.channel}**, con la ID **{ctx.message.channel.category_id}**,
en la categoría *{ctx.message.channel.category}*, con la ID **{ctx.message.channel.category.category_id}**, 
desde el servidor **{ctx.message.channel.guild}**, con la ID **{ctx.message.channel.guild.id}**,
con el comando **{ctx.message.content}**''')
