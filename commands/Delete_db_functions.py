from discord.ext import commands as client
import mysql.connector
from colorama import Fore, init


class DbCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot


init(True)


@client.command(name='deletedb')
async def drop_Db(self, ctx):
    database = ''
    if ctx.message.author.id == 780226351419621446 and ctx.message.author.name == 'Terma':
        await ctx.send('Esperando confirmación en la consola...')
        print(
            Fore.RED + 'ATENCION: ESTA ACCIÓN ES PERMANENTE Y PERDERA TODOS LOS DATOS ALMACENADOS.')
        opt = str(input(
            'Esta seguro de que desea eliminar la base de datos principal (discord)? Si | No: '))
        if opt == 'Si':
            try:
                database = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                )
            except mysql.connector.Error as e:
                await ctx.send('Acción cancelada debido a un problema en la conexión con la base de datos.')
                print(Fore.RED + 'ERROR || {}'.format(e))
            else:
                print(Fore.GREEN + 'Success: Database connection.')
            cursor = database.cursor()

            try:
                cursor.execute("DROP DATABASE discord;")
            except mysql.connector.Error as e:
                await ctx.send('Error. Revise la consola para más información')
                print(Fore.RED + 'ERROR || {}'.format(e))
            database.commit()
            database.close()

            print(Fore.GREEN + 'DB dropped successfully.')
            await ctx.send('La acción se ha realizado sin errores.')
        elif opt == 'No':
            print('Proceso cancelado.')
            await ctx.send('Acción cancelada por consola.')
        else:
            print('Opción inválida. Cancelando acción...')
            await ctx.send('Acción cancelada por consola.')
    else:
        await ctx.send('Acceso denegado.')


@client.command(name='deletetable')
async def dropTable(ctx):
    database = ''
    if ctx.message.author.id == 780226351419621446 and ctx.message.author.name == 'Terma':
        await ctx.send('Esperando confirmación en la consola...')
        print(Fore.RED + 'ATENCION: ESTA ACCIÓN ES PERMANENTE Y PERDERA TODOS LOS DATOS ALMACENADOS.')
        opt = str(
            input('Esta seguro de que desea eliminar la tabla principal (users)? Si | No: '))
        if opt == 'Si':
            try:
                database = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                )
            except mysql.connector.Error as e:
                await ctx.send('Acción cancelada debido a un problema en la conexión con la base de datos.')
                print(Fore.RED + 'ERROR || {}'.format(e))
            else:
                print(Fore.GREEN + 'Success: Database connection.')
            cursor = database.cursor()
            try:
                cursor.execute('DROP TABLE discord.users')
                database.commit()
                database.close()
            except mysql.connector.Error as e:
                print(Fore.RED + 'ERROR || {}'.format(e))
                await ctx.send('Error. Revise la consola para más información.')
            else:
                await ctx.send('La acción se ha realizado sin errores.')
                print(Fore.GREEN + 'Table dropped successfully.')
        elif opt == 'No':
            print('Proceso cancelado.')
            await ctx.send('Acción cancelada por consola.')
        else:
            print('Opción inválida. Cancelando acción...')
            await ctx.send('Acción cancelada por consola.')
    else:
        await ctx.send('Acceso denegado.')

    # @interClient.message_command(name='resend', guild_ids=[796825733137039431, 964964697038286858])
    # async def resend(ctx):
    #     await ctx.respond(f'`{ctx.message.content}`')
