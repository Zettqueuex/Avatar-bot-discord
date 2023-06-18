import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"ปลากะพงฮับ | {bot.user.name}"))

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    avatar_url = member.avatar_url_as(static_format='png')
    embed = discord.Embed(title=f'{member.display_name}\'s Avatar', description=f'**นี่คือภาพอวาตาของ** {member.mention}', color=discord.Color.blue())
    embed.set_image(url=avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)

bot.run('tokenbot')
