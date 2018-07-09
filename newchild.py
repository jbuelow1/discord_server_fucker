import discord

bot0 = discord.Client()
bot1 = discord.Client()
bot2 = discord.Client()

@bot0.event
@bot1.event
@bot2.event
async def on_ready():
    print('a bot is ready!')

bot0.start('NDY1NzM5Mjg4MzM2NzkzNjEy.DiUcCA.c6MrVb3J6vZrxMxowJmIW-ivxUc')
bot1.start('NDY1OTExMDE5NDEyMzg5ODg5.DiUcGw.81zxMeI4-PewqUeSbrEe7OAI2DM')
bot2.start('NDY1OTExNDc4NDQ1MTQ2MTEy.DiUcLQ.kiEqtmo6b6bLz26EZf5aepdImHo')
