import discord
from secretstuff import FLAG, TOKEN

client = discord.Client()
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    flagMaster = False
    for role in message.author.roles:
        if role.name == 'FlagMaster':
            flagMaster = True

    if message.content.startswith('$flag'):
        if flagMaster:
            await message.channel.send(f"Hi FlagMaster! Here's the flag:\n{FLAG}")
        else:
            await message.channel.send("Sorry, you don't have the FlagMaster role!")
    elif message.content.startswith('$help'):
        await message.channel.send("**FlagBot Help**\n$help - Show this help message\n$flag - Get flag")

client.run(TOKEN)
