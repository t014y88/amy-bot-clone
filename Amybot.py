# Token: NDQ5OTk4NjU4MjkzNzI3MjQz.Des1bg.Aley6Z9_iZBgbuQKHpSOXj4LWTo

# ID: 449998658293727243

# Rules channel: : 433893996595642368

# Report channel : 449779652240605185

# Bot 1 : 433900499532775424

# Bot 2 : 433900512556089346

import discord
from discord.ext import commands
from discord.utils import get
import random
import asyncio
import logging
import time

bot = commands.Bot(command_prefix='amy/', description='Uhhhhhhhhhhhhhhhhhhhhhh')
bot.remove_command('help')
client = discord.Client

@commands.has_permissions(manage_messages=True, manage_roles=True)

@bot.event
async def on_ready():
    print("I am ready master...")

@bot.command()
async def hello(ctx):
    if ctx.message.channel.id == (433900499532775424 or 433900512556089346):
        await ctx.send("hello")
    
@bot.command()
async def report(ctx, *, stuff):
    time = ctx.message.created_at
    repochan = bot.get_channel(449779652240605185)
    user = ctx.message.author
    await ctx.message.delete()
    embed = discord.Embed(title="Report by {}".format(ctx.message.author.name), color=0xff0000)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.add_field(name="ID", value=ctx.message.author.id, inline=True)
    embed.add_field(name="Channel", value=ctx.channel, inline=True)
    embed.add_field(name="Report", value=stuff, inline=True)
    embed.set_footer(text=time)
    await repochan.send(embed=embed)
    await user.send('Report sent.')

@bot.command()
async def mlady(ctx, name):
    if ctx.message.channel.id == (433900499532775424 or 433900512556089346):
        part1 = name[0]
        part2 = name[2:]
        await ctx.message.channel.send(part1 + '\'' + part2)

@bot.command()
async def sus(ctx):

    sadlist = [
    'Socially',
    'Surprisingly',
    'Suspiciously',
    'Sarcastically',
    'Simply',
    'Sadly',
    'Serendipitously',
    'Savagely',
    'Stylishly',
    'Scarily',
    'Seemingly',
    'Seldom',
    'Sheepishly',
    'Silently',
    'Sleepily',
    'Solemnly',
    'Solidly',
    'Suddenly',
    'Supposedly',
    'Soon to be',
    'Stealthily',
    'Sexually',
    'Saltily',
    'Strangely']

    uadlist = ['Unusual',
    'Unexpected',
    'Ubiquitous',
    'Unconventional',
    'Uninhibited',
    'Ugly',
    'Unkempt',
    'Unsightly',
    'Unimpressive',
    'Uptight',
    'Uneven',
    'Ultimate',
    'Unconscious',
    'Unequaled',
    'Unfortunate',
    'Unique',
    'Unlawful',
    'Unnatural',
    'Unripe',
    'Unwieldy',
    'Unwritten',
    'Upbeat',
    'Urban',
    'Underappreciated',
    'Used',
    'Useless']

    snolist = ['Solutions',
    'Sarcasm',
    'SuS-chan',
    'Stupidity',
    'Salmon',
    'Sachets',
    'Salt',
    'Saturdays',
    'Sacrifices',
    'Stuart',
    'Swords',
    'Spaghetti',
    'Sales Assistants',
    'Socialism',
    'Sableye',
    'Slinkies',
    'Serpents',
    'Silliness',
    'Subjugation']

    sad = random.choice(sadlist)
    uad = random.choice(uadlist)
    sno = random.choice(snolist)

    if ctx.message.channel.id == (433900499532775424 or 433900512556089346):
        await ctx.message.channel.send('S- ' + sad + '\nU- ' + uad + '\nS- ' + sno)

@bot.command()
async def help(ctx):
    user = ctx.message.author
    await ctx.message.delete()
    embed = discord.Embed(title='AmyBot Help', description='Commands for AmyBot', color=0xa80000)
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/441695556683956228.png?v=1')
    embed.add_field(name='amy/hello', value='AmyBot replies hello!', inline=True)
    embed.add_field(name='amy/report [report]', value='Use this to report incidents to the staff.', inline=True)

    await user.send(embed=embed)

@bot.command()
async def slap(ctx, user: discord.User):
    if ctx.message.channel.id == (433900499532775424 or 433900512556089346):
        channel = ctx.message.channel
        giflist = [
        'https://media.giphy.com/media/t1CsJ1o1sdOHm/giphy.gif',
        'https://media.giphy.com/media/EpuqRnJ0nbZ4Y/giphy.gif',
        'https://media.giphy.com/media/3eKfsCZKKb3c4/giphy.gif',
        'https://media.giphy.com/media/reXcrlJ3OhvDq/giphy.gif',
        'https://m.popkey.co/d5f999/4Vv51_s-200x150.gif',
        'https://media.giphy.com/media/l2SpSQLpViJk9vhmg/giphy.gif',
        'https://media.giphy.com/media/g0BHaJUquwEpO/giphy.gif',
        'https://media.giphy.com/media/Z7GYQ8Mq6uk6c/giphy.gif',
        'https://media.giphy.com/media/j3iGKfXRKlLqw/giphy.gif',
        'http://www.gifimagesdownload.com/wp-content/uploads/2016/02/latest-slap-gif-781.gif',
        'https://media.giphy.com/media/OxV8bANZdAvC0/giphy.gif',
        'http://p.fod4.com/p/media/87b82bdcd4/S79R0wSIW83Cpp0gFwn2_Shaving%20Cream%20Slap.gif',
        'https://www.reactiongifs.us/wp-content/uploads/2014/08/slap_archer.gif',
        'http://gifon007.eu/wp-content/uploads/2016/07/bud-spencer-a-terence-hill-slap.gif'
        ]
        gif = random.choice(giflist)
        embed = discord.Embed(color=0xa80000)
        embed.set_image(url=gif)
        await channel.send(content='{} slapped {}!'.format(ctx.message.author.mention, user.mention), embed=embed)

@bot.command()
async def kick(ctx, user: discord.Member, *, shit):
    if 'junior discord mods' in [y.name.lower() for y in ctx.message.author.roles] or 'senior discord mods' in [y.name.lower() for y in ctx.message.author.roles] or '/r/ddlc mods' in [y.name.lower() for y in ctx.message.author.roles]:
        await user.send('You have been kicked from the r/DDLC Official Discord.\nReason: {}'.format(shit))
        await user.kick(reason=shit)

@bot.command()
async def ban(ctx, user: discord.Member, *, shit):
    if 'senior discord mods' in [y.name.lower() for y in ctx.message.author.roles] or '/r/ddlc mods' in [y.name.lower() for y in ctx.message.author.roles]:
        await user.send('You have been banned from the r/DDLC Official Discord.\nReason: {}'.format(shit))
        await user.ban(reason=shit)

@bot.command()
async def warn(ctx, user: discord.Member, *, shit):
    if 'junior discord mods' in [y.name.lower() for y in ctx.message.author.roles] or 'senior discord mods' in [y.name.lower() for y in ctx.message.author.roles] or '/r/ddlc mods' in [y.name.lower() for y in ctx.message.author.roles]:
        embed = discord.Embed(title='Warning', description='You have been warned by r/DDLC Official Discord staff.', color=0xa80000)
        embed.add_field(name='Warning reason:', value='{}'.format(shit), inline=True)
        await user.send(embed=embed)

@bot.command()
async def userinfo(ctx, user: discord.Member):
    if ctx.message.channel.id == (433900499532775424 or 433900512556089346):
        channel = ctx.message.channel
        embed = discord.Embed(title=user.name + '\'s info', description='Information on this user.', color=0xa80000)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name='ID:', value=user.id, inline=True)
        embed.add_field(name='Top Role:', value=user.top_role, inline=True)
        embed.add_field(name='Joined on:', value=user.joined_at, inline=True)
        await channel.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    if ctx.message.channel.id == (433900499532775424 or 433900512556089346):
        channel = ctx.message.channel
        server = ctx.guild
        embed = discord.Embed(title='/r/DDLC Discord Info', description='Server info.', color=0xa80000)
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name='ID:', value=server.id)
        embed.add_field(name='Owner:', value=server.owner)
        embed.add_field(name='Creation date:', value=server.created_at)
        embed.add_field(name='Members:', value=server.member_count)
        await channel.send(embed=embed)

bot.run('NDQ5OTk4NjU4MjkzNzI3MjQz.Des1bg.Aley6Z9_iZBgbuQKHpSOXj4LWTo')



