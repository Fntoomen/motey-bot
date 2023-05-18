import discord
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.message_content = True

client = Bot(command_prefix='', intents=intents)

@client.command()
async def aha(ctx):
        await ctx.message.delete()
        webhook = await ctx.channel.create_webhook(name=ctx.author.nick)
        await webhook.send(
            'https://cdn.7tv.app/emote/6287c2ca6d9cd2d1f31b5e7d/4x.gif', username=ctx.author.name, avatar_url=ctx.author.avatar)

        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
                await webhook.delete()

@client.command()
async def xdd(ctx):
        await ctx.message.delete()
        webhook = await ctx.channel.create_webhook(name=ctx.author.nick)
        await webhook.send(
            'https://cdn.7tv.app/emote/613937fcf7977b64f644c0d2/3x.webp', username=ctx.author.name, avatar_url=ctx.author.avatar)

        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
                await webhook.delete()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run('TOKEN')
