import discord
import random
import mysql.connector


db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="passwd",
	database="emotebot"
)

crsr = db.cursor()
crsr.execute("SELECT * FROM emotes")

emotes = crsr.fetchall()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

counter = 0


@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	for emote in emotes:
		if message.content == emote[0]:
			# delete the message (at the start to avoid 404s)
			await message.delete()

			# replace text with emote
			with open(emote[1], "rb") as f:
				picture = discord.File(f)
			# print the message as user
				webhook = await message.channel.create_webhook( name=message.author.name )
				await webhook.send( file=picture,
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
		emote = random.choice(emotes)
		with open(emote[1], "rb") as f:
			msg = "RANDOM EMOTE"
			picture = discord.File(f)
			await message.channel.send(msg, file=picture)

		counter = 0
		return


client.run('TOKEN')
