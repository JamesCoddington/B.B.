import random
import discord
import datetime
from analysis import analyze
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)

@bot.command()
async def whyISuck(ctx):
    excuses = ["No excuses",]
    await ctx.send(excuses[0])
    
@bot.command()
async def calc(ctx, *args):
    try:
        excuses = ["My cat jumped onto my keyboard and accidentally unplugged my mouse, making it impossible for me to aim properly.",
               "I was trying to play with my feet because I heard it improves reaction time, but it turns out I'm not quite as ambidextrous as I thought.",
               "I was too busy analyzing the psychology behind the enemy team's strategic plays to actually execute any of my own.",
               "My character had a sudden allergic reaction to the smoke grenades, leaving me temporarily blinded and disoriented.",
               "I was having a philosophical debate with my teammate about the nature of winning, and whether it was really important in the grand scheme of things.",
               "I was testing out a new keyboard with a different key layout and accidentally pressed the wrong keys every time.",
               "I was too busy practicing my dance moves during the round transitions to remember to focus on the game.",
               "I was trying to see how long I could play with my eyes closed and still do well. Spoiler alert: not very long.",
               "I was trying to use a sniper rifle with a controller instead of a mouse and keyboard, and it turns out that's not a great idea.",
               "I was trying to break my personal record for how many times I could spin around before firing, and ended up just making myself dizzy.",
               "I was experiencing some severe lag and my character was moving in slow motion, making it impossible to keep up with the rest of the team.",
               "I was trying to play with chopsticks as a fun challenge, but they kept slipping out of my hands and hitting the wrong keys.",
               "I was too busy admiring the intricate details on my character's gloves to pay attention to the game.",
               "I was trying to play while standing on my head for a better view of the screen, but it turns out that's not very conducive to accurate aiming.",
               "I accidentally spilled some hot sauce on my mousepad, making it too slippery to properly control my aim.",
               "I was too busy practicing my singing skills during the respawn times to focus on the game.",
               "I was distracted by a moth flying around my monitor, and ended up getting killed while trying to catch it.",
               "I was trying to play while wearing a blindfold as a fun challenge, but it turns out that's not a great way to win matches.",
               "I was trying to play while juggling three oranges as a fun challenge, but it turns out that's not a great way to maintain focus.",
               "I was having an intense internal debate about whether I should play aggressively or passively, and ended up getting caught in no man's land.",]
        random_number = random.randint(0, 19)
        message = ' '.join(args)
        await ctx.send(f"{message} \n {excuses[random_number]}")
    except Exception as e:
        await ctx.send("Invalid input. Please enter numbers only.")

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     else:
#         if message.channel.id == "test-onmessage":
        
#             sentences = [
#                 "Hello, world!",
#                 "I like turtles.",
#                 "The quick brown fox jumps over the lazy dog.",
#                 "This is a random sentence.",
#                 "Python is a great language.",
#                 "I am a bot.",
#                 "How are you today?",
#                 "Have a nice day!",
#                 "What's your favorite color?",
#                 "This sentence is false.",
#                 "To be or not to be?",
#                 "That is the question.",
#                 "Roses are red, violets are blue...",
#                 "Why did the chicken cross the road?",
#                 "Because it wanted to get to the other side."
#             ]
#             random_sentence = random.choice(sentences)
#             await message.channel.send(random_sentence)

@bot.command()
async def sweep(ctx, member: discord.Member):
    user_messages = []

    start_time = datetime.datetime.utcnow() - datetime.timedelta(days=7)
    for channel in ctx.guild.text_channels:
        async for message in channel.history(after=start_time):
         if message.author.id == member.id:
              print(channel.name)
              if(channel.name == "bot-commands"):
                print(message.content)
              user_messages.append(message.content)

    analysis_score = analyze(user_messages)
    if (analysis_score > .2):
        await member.kick(reason="B.B. Activated")
        await ctx.send(f"{member} has been kicked for having an aggression score of {analysis_score}")

    await ctx.send(analyze(user_messages))


bot.run('')