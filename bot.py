import discord
import datetime
from analysis import analyze
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)
client = discord.Client(intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        if message.content.startswith('!check'):
            await check(message)
        await sweep(message)


async def get_analysis_score(message):
    ctx = await bot.get_context(message)
    user_messages = []
    member = message.author
    start_time = datetime.datetime.utcnow() - datetime.timedelta(days=7)

    for channel in ctx.guild.text_channels:
        async for message in channel.history(after=start_time):
            if message.author.id == member.id:
                user_messages.append(message.content)

    analysis_score = analyze(user_messages)
    return analysis_score


async def check(message):
    ctx = await bot.get_context(message)
    member = message.author
    analysis_score = await get_analysis_score(message)
    await ctx.send(f"{member} has an aggression score of {analysis_score}")


async def sweep(message):
    ctx = await bot.get_context(message)
    member = message.author
    analysis_score = await get_analysis_score(message)

    if (analysis_score > .3):
        await member.kick(reason="B.B. Activated")
        await ctx.send(f"{member} has been kicked for having an aggression score of {analysis_score}")


bot.run("REPLACE WITH PROVIDED TOKEN")
