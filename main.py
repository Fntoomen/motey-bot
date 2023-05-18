import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('xdd'):
        await message.channel.send('https://cdn.7tv.app/emote/613937fcf7977b64f644c0d2/4x.webp')
        await message.delete()
    if message.content.startswith('aha'):
        await message.channel.send('https://cdn.7tv.app/emote/6287c2ca6d9cd2d1f31b5e7d/4x.gif')
        await message.delete()

client.run('TOKEN')
