import discord
import random



intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


counter = 0

emotes = {
    'xdd': 'https://cdn.7tv.app/emote/613937fcf7977b64f644c0d2/3x.webp',
    'aha': 'https://cdn.7tv.app/emote/6287c2ca6d9cd2d1f31b5e7d/4x.gif',
    'Nerd': 'https://cdn.7tv.app/emote/6134bc74f67d73ea27e44b0f/4x.gif',
    'oKurwa': 'https://tenor.com/view/okurwa-kurwa-stachujones-stachu-jones-gif-13138130',
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
    'GIGACHAD': 'https://cdn.7tv.app/emote/60ae958e229664e8667aea38/4x.gif',
    'MONKE': 'https://cdn.7tv.app/emote/60ae6bc786fc40d488d98cbd/4x.gif',
    'xd': 'https://cdn.7tv.app/emote/60773136a807bed006130b28/4x.gif',
    'LMAO': 'https://cdn.7tv.app/emote/60ae4b670e354776345e6c19/4x.gif',
    'Tssk': 'https://cdn.7tv.app/emote/60ae387cb2ecb0150505e235/4x.gif',
    'Madge': 'https://cdn.7tv.app/emote/60a95f109d598ea72fad13bd/4x.webp',
    'Okayge': 'https://cdn.7tv.app/emote/605391a99d9e96000d244fd0/4x.webp',
    'Weirdge': 'https://cdn.7tv.app/emote/604a93564d948c001460998b/4x.webp',
    'NOPERS': 'https://cdn.7tv.app/emote/604097c3cf6746000db10344/4x.gif',
    'pepeJAM': 'https://cdn.7tv.app/emote/6040a8bccf6746000db10348/4x.gif',
    'FloppaHey': 'https://cdn.7tv.app/emote/6043b2b31d4963000d9dae68/4x.gif',
    'BRUHBRUH': 'https://cdn.7tv.app/emote/603f4fc7115b55000d728300/4x.gif',
    'Floppas': 'https://cdn.7tv.app/emote/603eb97c115b55000d7282ec/4x.gif',
    'peepoGlad': 'https://cdn.7tv.app/emote/603d32e968a0fc000dfdda1a/4x.webp',
    'Sadge': 'https://cdn.7tv.app/emote/603cac391cd55c0014d989be/4x.webp',
    'Okayeg': 'https://cdn.7tv.app/emote/603caa69faf3a00014dff0b1/4x.webp',
    'uuu': 'https://tenor.com/view/kizo-polska-poland-song-uuuu-ajajaj-gif-24409594',
    'XD': 'https://cdn.discordapp.com/attachments/1111737407931424808/1111738118173892638/Z.png',
    'livesey': 'https://tenor.com/view/venom-treasure-island-dr-livesey-livesey-megaboss-gif-26407339',
    'chad': 'https://cdn.discordapp.com/attachments/1111737407931424808/1111738440271273994/279196103_1168316163927514_6190201642596978640_n.png',
    '2137': 'https://tenor.com/view/jan-pawe%C5%822-jan-pawe%C5%82-jan-pawe%C5%82-jp2-gif-18747767',
    'furas': 'https://tenor.com/view/furry-meme-missile-furry-alert-gif-24658735',
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
            # delete the message (at the start to avoid 404s)
            await message.delete()

            # replace text with emote
            msg = emotes[emote]

            # print the message as user
            webhook = await message.channel.create_webhook( name=message.author.name )
            await webhook.send( msg,
 username=message.author.name,
 avatar_url=message.author.avatar )

            # delete the webhook
            await webhook.delete()

            return


    if "windows" in message.content.lower():
        # Windows = DIESOFCRINGE
        msg = "I FUCKIN' LOVE WINDOWS 'N ADS!"

        # print the message as user
        webhook = await message.channel.create_webhook( name=message.author.name )
        await webhook.send( msg,
username=message.author.name,
avatar_url=message.author.avatar )

        # clean up
        await webhook.delete()

        return


    global counter
    counter += 1

    if counter >= 50:
        msg = random.choice(list(emotes.values()))
        await message.channel.send(msg)
        counter = 0

        return



client.run('TOKEN')
