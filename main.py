import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

emotes = {
 'xdd': 'https://cdn.7tv.app/emote/613937fcf7977b64f644c0d2/3x.webp',
 'aha': 'https://cdn.7tv.app/emote/6287c2ca6d9cd2d1f31b5e7d/4x.gif',
 'Nerd': 'https://cdn.7tv.app/emote/6134bc74f67d73ea27e44b0f/4x.gif',
 'oKurwa': 'https://media.tenor.com/xMbga2RiU1IAAAAC/o-kurwa-stachu-jones.gif',
 'catKISS': 'https://cdn.7tv.app/emote/60a1babb3c3362f9a4b8b33a/4x.gif',
 'jasperJAM': 'https://cdn.7tv.app/emote/60aeb51cd970a5b9cfc1ba08/4x.gif',
 'witamCieKolezanko': 'https://cdn.7tv.app/emote/60ae7f2580dd689cc780be94/4x.gif',
 'moin': 'https://cdn.7tv.app/emote/60ae930b98f42914705c4910/4x.gif',
 'muza': 'https://cdn.7tv.app/emote/60aeae60f39a7552b6eeff5e/4x.gif',
 'demonzXXX': 'https://cdn.7tv.app/emote/60aea8b9ea50f43c9e28ae78/4x.gif',
 'KTURAGODZINA': 'https://cdn.7tv.app/emote/60aebaf96cfcffe15fabe77c/4x.gif',
 'segz': 'https://cdn.7tv.app/emote/60b00436aecc11e86cb96dd7/4x.gif',
 'jasperPompki': 'https://cdn.7tv.app/emote/60b030c3b3e1671e27940d53/4x.gif',
 'jasperCola': 'https://cdn.7tv.app/emote/60b252030fc2b1dc12b7a9f7/4x.gif',
 'Dance': 'https://cdn.7tv.app/emote/60b3c994e6585cf119a1ed57/4x.gif',
 'wuda': 'https://cdn.7tv.app/emote/60b4f64435d6af7b69132aa0/4x.gif',
}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    for emote in emotes.keys():
        if message.content == emote:
            # replace text with emotes
            msg = emotes[emote]

            # print the message as user
            webhook = await message.channel.create_webhook( name=message.author.name )
            await webhook.send( msg,
 username=message.author.name,
 avatar_url=message.author.avatar )
            webhooks = await message.channel.webhooks()

            # clean up
            for webhook in webhooks:
                    await webhook.delete()
            await message.delete()

client.run('TOKEN')
