import discord
import random
import mariadb
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

conn = mariadb.connect (
        host="localhost",
        user="root",
        password="passwd",
        database="emote"
        )
cur = conn.cursor()

activity = discord.Activity(type=discord.ActivityType.watching, name="YOUR MOM")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents, activity=activity)

counter = 0

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    cur.execute("SELECT location FROM emotes WHERE name = %s", (message.content,))
    emoteLocation = cur.fetchone()
    if emoteLocation is not None:
        emoteLocation = emoteLocation[0]
        cur.execute("UPDATE emotes SET times_used = times_used +1 WHERE location = %s", (emoteLocation,))
        conn.commit()
        # delete the message (at the start to avoid 404s)
        await message.delete()
        # replace text with emote
        with open(emoteLocation, "rb") as f:
            picture = discord.File(f)
            # print the message as user
            webhook = await message.channel.create_webhook( name=message.author.name )
            await webhook.send(file=picture,
                               username=message.author.name,
                               avatar_url=message.author.avatar)
            # delete the webhook
            await webhook.delete()
        return

    if "windows" in message.content.lower():
        # Windows = DIESOFCRINGE
        msg = "I FUCKIN' LOVE ADS!"
        # print the message as user
        webhook = await message.channel.create_webhook( name=message.author.name )
        await webhook.send(msg,
                           username=message.author.name,
                           avatar_url=message.author.avatar)
        # clean up
        await webhook.delete()
        return

    global counter
    counter += 1
    if counter >= 50:
        cur.execute("SELECT COUNT(name) FROM emotes")
        emotesCount = cur.fetchone()
        if emotesCount is not None:
            emotesCount = emotesCount[0]
        randomNumber = random.randint(1, emotesCount)
        cur.execute("SELECT location FROM emotes WHERE id = %d", (randomNumber,))
        emoteLocation = cur.fetchone()
        if emoteLocation is not None:
            emoteLocation = emoteLocation[0]
        cur.execute("SELECT name FROM emotes WHERE id = %d", (randomNumber,))
        emoteName = cur.fetchone()
        if emoteName is not None:
            emoteName = emoteName[0]
        with open(emoteLocation, "rb") as f:
            msg = f"Random emote: {emoteName}"
            picture = discord.File(f)
            await message.channel.send(msg, file=picture)
        counter = 0
        return

client.run('TOKEN')
conn.close()
