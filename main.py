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

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

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
                               username=message.author.nick,
                               avatar_url=message.author.avatar)
            # delete the webhook
            await webhook.delete()
        return

client.run('TOKEN')
conn.close()
