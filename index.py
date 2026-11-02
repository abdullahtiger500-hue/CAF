import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ضع آيدي الروم الصوتي هنا بين الأقواس
CHANNEL_ID = 1565879563236540416 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.connect()
        print("تم الدخول للروم الصوتي بنجاح!")

# ضع توكن البوت الخاص بك هنا بين علامتي التنصيص
bot.run("MTU2Njc3MzY2NDMzNzI0MDE3NQ.GZjIuE.FGRKINHiX0rq8KuQxKq5kUKUSPI480yq1-0VeE")