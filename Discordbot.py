import json
from os import system
from discord.ext import commands
from sys import argv
import discord

# Import commands from commands folder
from commands.Key_Generator import GeneratorCog
from commands.Rock_Paper_Scissors import RpsCog
from commands.Port_Scan import PortscanCog
from commands.Mc_Server import McCog
from commands.Text_to_Speech import StartCog
from commands.Timer_Countdown import TimerCog
from commands.All_Commands import CommandsCog
from commands.Sum import SumCog
from commands.Loop import LoopCog
from commands.Login_Register import QueryCog
from commands.Delete_db_functions import DbCog
from commands.Youtube_query import QYoutubeCog
from commands.Sv_info import SvInfoCog
from commands.talk_to_dm import TalktoDMCog

dev_mode = False

client = commands.Bot(command_prefix='t!', description='Use t! for my commands!. t!commands for all commands.', intents=discord.Intents.default())

# Initialize imported commands
client.add_cog(LoopCog(client))
client.add_cog(StartCog(client))
client.add_cog(PortscanCog(client))
client.add_cog(TimerCog(client))
client.add_cog(CommandsCog(client))
client.add_cog(DbCog(client))
client.add_cog(QueryCog(client))
client.add_cog(RpsCog(client))
client.add_cog(SumCog(client))
client.add_cog(GeneratorCog(client))
client.add_cog(McCog(client))
client.add_cog(QYoutubeCog(client))
client.add_cog(SvInfoCog(client))
client.add_cog(TalktoDMCog(client))

bot_version = '1.0.0'
bot_owner = '780226351419621446'


@client.event
async def on_ready():
    system('cls')
    print('Bot successfully started!\n')


@client.event
async def on_message(message: discord.Message):
    for mention in message.mentions:
        if mention.name == 'Terma':
            await message.channel.send('He is AFK!')


if len(argv) != 1:
    if argv[1] == '-dev_mode':
        dev_mode = True
        print(f'Running {argv[0]} in developer mode...')


@client.command(name='about')
async def dev_mode(ctx):
    if dev_mode:
        await ctx.send('Bot is currently in developer mode.')


msg_id = ''


@client.command(name='reaction')
async def reaction_add(ctx):
    global msg_id
    await ctx.message.add_reaction('🐱')
    msg_id = ctx.message.id


@client.command(name='check')
async def check_reactions(ctx):
    async for message in ctx.channel.history(limit=5):
        if message.id == msg_id:
            await ctx.send('Encontre el mensaje.')
            for reaction in message.reactions:
                await ctx.send(f'{reaction.emoji} tiene {reaction.count} reacciones ')


def loadToken(ruta):
    with open(ruta) as content:
        token = json.load(content)
        return token.get('token')


client.run(loadToken('token.json'))
