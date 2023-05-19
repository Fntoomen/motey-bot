import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

emotes = {'xdd': 'https://cdn.7tv.app/emote/613937fcf7977b64f644c0d2/3x.webp', 'aha': 'https://cdn.7tv.app/emote/6287c2ca6d9cd2d1f31b5e7d/4x.gif', 'nerd': 'https://cdn.7tv.app/emote/6134bc74f67d73ea27e44b0f/4x.gif', 'kurwa': 'https://media.tenor.com/xMbga2RiU1IAAAAC/o-kurwa-stachu-jones.gif'}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if any( message.content == emote for emote in emotes.keys() ):
        # replace text with emotes
        msg = message.content
        msg = msg.replace( k, emotes[k] )

        # print the message as user
        webhook = await message.channel.create_webhook( name=message.author.name )
        await webhook.send( msg, username=message.author.name, avatar_url=message.author.avatar )
        webhooks = await message.channel.webhooks()

        # clean up
        for webhook in webhooks:
                await webhook.delete()
        await message.delete()

client.run('TOKEN')
