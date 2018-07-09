import discord
import random
import os
from six.moves import configparser

payload = '@everyone\n<@250803093049049089><@254683345735254016><@347507600541089793><@347735227055210496>\nhttps://media.giphy.com/media/PqXQV58Tva7DO/giphy.gif\nhttps://media.giphy.com/media/hLx1RYpEamdj2/giphy.gif\nhttps://media.giphy.com/media/xARspuzI2RZCw/giphy.gif\nhttps://media.giphy.com/media/11hEdGzcUswSEU/giphy.gif\nhttps://media.giphy.com/media/2qADsl3oMNtsc/giphy.gif\n**ITS SPAM TIME MY NI:b::b:AS**'
notify = True
counter = 0

bot = discord.Client()

@bot.event
async def on_ready():
    print('API connected!')

    print('Setting icon and name...')
    file = open('icon.png', 'rb')
    try:
        await bot.user.edit(username='Squidward Child', avatar=file.read())
    except:
        pass

    print('Ready to spam!')

@bot.event
async def on_message(message):
    if message.author.bot:
        if notify:
            print('Spam has bugun.')
            notify = not notify
        if message.mention_everyone:
            counter += 1
            if counter % 100:
                print('All the bots total have spammed @everyone ' + counter + ' times!')
        await message.channel.send(payload)

filename = "bot.cfg"
if os.path.isfile(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    token = config.get("config", "token")
else:
    print('NO CONFIG FOUND')
    exit(1)

bot.run(token)
