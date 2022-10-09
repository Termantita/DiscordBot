from discord.ext import commands as client
import mysql.connector
from colorama import init, Fore

init(True)


class Users:
    def __init__(self, user, password, msg_author, author_id):
        self.user = user
        self.password = password
        self.msg_author = msg_author
        self.author_id = int(author_id)


class QueryCog(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(name='login')
    async def client_login(self, ctx, *, arg):
        print('Client login:')
        try:
            database = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="discord",
            )
        except mysql.connector.Error as e:
            await ctx.send('Error. Puede que la base de datos esté apagada.')
            print(Fore.RED + 'ERROR || {}'.format(e))
        else:
            print(Fore.GREEN + 'Success: Database connection.')

            u, p = arg.split(' ')
            if len(u) < 3 or len(p) < 3:
                await ctx.send('Los datos ingresados deben ser mayor a 2 carácteres.')
            else:
                cursor = database.cursor()
                sql = "SELECT user, password FROM users WHERE user = %s AND password = %s;"
                val = (u, p)
                try:
                    cursor.execute(sql, val)
                except Exception as e:
                    await ctx.send('Ocurrio un error al pedir los datos en la base de datos.')
                    print(Fore.RED + 'ERROR || {}'.format(e))

                result = cursor.fetchone()

                print(result)

                if result is not None:
                    info = {
                        'user': result[0],
                        'password': result[1]
                    }

                    await ctx.send('Sesión iniciada.')
                    await ctx.send('Datos:')
                    await ctx.send(f'Usuario: ' + str(info['user']))
                    await ctx.send(f'Contraseña: ' + str(info['password']))
                else:
                    await ctx.send('Usuario y/o contraseña no válidos.')

    # Entrada esperada: t!register Terma 123
    @client.command(name='register')
    async def client_register(self, ctx, *, arg):
        database = ''
        print('Client registration:')
        symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%',
                   '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$',
                   ')',
                   '/'}
        try:
            database = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
            )
        except mysql.connector.Error as e:
            await ctx.send('Error. Puede que la base de datos esté apagada.')
            print(Fore.RED + 'ERROR || {}'.format(e))
        else:
            print(Fore.GREEN + 'Success: Database connection.')
        cursor = database.cursor()

        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS discord;")
        except mysql.connector.Error as e:
            # print(Fore.RED + 'Error in Query: Create DB.')
            print(Fore.RED + 'ERROR || {}'.format(e))
        else:
            print(Fore.GREEN + 'Success: Access to database.')

        try:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS discord.users (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, user VARCHAR(50) "
                "NOT NULL UNIQUE, password VARCHAR(30) NOT NULL, discord_user VARCHAR(100) NOT NULL, user_id INT(50) NOT "
                "NULL);")
        except mysql.connector.Warning as e:
            print()
            # print(Fore.RED + 'Error in Query: Create table.')
            print(Fore.RED + 'ERROR || {}'.format(e))
        else:
            print(Fore.GREEN + 'Success: Access to table.')

        for i in arg:
            if i in symbols:
                await ctx.send(
                    'Los símbolos o carácteres especiales (@, #, &, etc...) no están permitidos como usuario o '
                    'contraseña. Intente nuevamente.')
                print(Fore.RED + 'ERROR || Symbols are not allowed in user/password.')
                raise NameError(
                    Fore.RED + 'ERROR || Symbols are not allowed in user/password.')

        u, p = arg.split(' ')

        account = Users(u, p, ctx.message.author.name, ctx.message.author.id)

        sql = "INSERT INTO discord.users (user, password, discord_user, user_id) VALUES (%s, %s, %s, %s);"
        val = (account.user, account.password,
               account.msg_author, account.author_id)

        try:
            cursor.execute(sql, val)
        except mysql.connector.Error as e:
            await ctx.send('Error desconocido al intentar guardar los datos. (A lo mejor el usuario ya existe?)')
            print(Fore.RED + 'ERROR || {}'.format(e))
            print('End.')
        else:
            database.commit()
            await ctx.send('Los datos se guardaron correctamente!')
            print(Fore.GREEN + 'Success: Registration')
            print('End.')

            database.close()

            print('\n')
