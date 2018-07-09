import discord

bot = discord.Client()
count = 0

@bot.event
async def on_ready():
    print('Ready!')

@bot.event
async def on_message(message):
    if message.mentions_everyone:
        count += 1
        if count % 100 == 0:
            print('The squiddies have pinged @everyone ' + str(count) + ' times!')

bot.run('')
