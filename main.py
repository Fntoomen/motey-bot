import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    server = client.get_guild(1087681051515691008)
    global bot
    bot = server.get_member(1108722454353948692)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('xdd'):
        await bot.edit(nick=message.author.nick)
        await message.channel.send('https://cdn.7tv.app/emote/613937fcf7977b64f644c0d2/3x.webp')
        await message.delete()

client.run('TOKEN')
