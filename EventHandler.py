import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='amy/', description='Uhhhhhhhhhhhhhhhhhhhhhh')
client = discord.Client
reacmsg = None

@bot.event
async def on_ready():
    print('EventHandler activated.')
    discord.Permissions(permissions=0x10000000)

@bot.event
async def on_message(message):

    if message.content.startswith('amy/msgid'):
        print(message.id)

    if message.content.startswith('amy/roleselect') and message.channel.name == 'place-of-joining' and '/r/ddlc mods' in [y.name.lower() for y in message.author.roles]:
        msg = message.channel

        embed = discord.Embed(title='Team Selection', description='React to select a team!', color=0xff00cb)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/doki-doki-literature-club/images/c/c9/Logo.png/revision/latest?cb=20171204125056')
        embed.add_field(name='🏹', value='Joins Team Sayori', inline=True)
        embed.add_field(name='🔪', value='Joins Team Yuri', inline=True)
        embed.add_field(name='🍰', value='Joins Team Natsuki', inline=True)
        embed.add_field(name='💚', value='Joins Team Monika', inline=True)
        embed.add_field(name='🅱', value='Joins Team Protag', inline=True)
        embed.add_field(name='🕷', value='Joins Team Amy', inline=True)
        embed.add_field(name='✅', value='Joins Team ADBD (All Dokis Best Doki)', inline=True)
        embed.add_field(name='Notice:', value='By selecting a team, you acknowledge that you have read and will adhere to all of the rules listed in the rules tab. Breaking these rules will lead to possible punishment.')

        botmsg = await msg.send(embed=embed)

        await botmsg.add_reaction('🏹')
        await botmsg.add_reaction('🔪')
        await botmsg.add_reaction('🍰')
        await botmsg.add_reaction('💚')
        await botmsg.add_reaction('🅱')
        await botmsg.add_reaction('🕷')
        await botmsg.add_reaction('✅')

        global msgid
        msgid = botmsg.id
        
    if message.author != bot.user:    
        sub = message.content.split(' ')
        for word in sub:
            channel = message.channel
            if (word[0] == 'r' or word[0] == 'R' or word[0] == 'u' or word[0] == 'U') and word[1] == '/':
                await channel.send('https://www.reddit.com/' + word)
                break
            if word.lower() == 'i\'m' or word.lower() == 'im':
                parts = message.content.split(word)
                name = parts[1]
                await channel.send('Hi' + name + ', I\'m Dad!')
                break
            if word.lower() == 'fucking' or word.lower() == 'fuckin':
                parts = message.content.split(word + ' ')
                parts2 = str(parts[1])
                parts3 = parts2.split(' ')
                await channel.send('As opposed to normal ' + parts3[0])
                break

@bot.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    print(msgid)
    if 'new' in [y.name.lower() for y in user.roles]:
        if reaction.emoji == '🏹' and msg.id == msgid:
            print('Sayori role given')
            role = discord.utils.find(lambda r: r.name == 'Team Sayori', msg.guild.roles)
            await user.add_roles(role)
            role2 = discord.utils.find(lambda r: r.name == 'Member', msg.guild.roles)
            await user.add_roles(role2)
            role3 = discord.utils.find(lambda r: r.name == 'New', msg.guild.roles)
            await user.remove_roles(role3)
        if reaction.emoji == '🔪' and msg.id == msgid:
            print('Yuri role given')
            role = discord.utils.find(lambda r: r.name == 'Team Yuri', msg.guild.roles)
            await user.add_roles(role)
            role2 = discord.utils.find(lambda r: r.name == 'Member', msg.guild.roles)
            await user.add_roles(role2)
            role3 = discord.utils.find(lambda r: r.name == 'New', msg.guild.roles)
            await user.remove_roles(role3)
        if reaction.emoji == '🍰' and msg.id == msgid:
            print('Natsuki role given')
            role = discord.utils.find(lambda r: r.name == 'Team Natsuki', msg.guild.roles)
            await user.add_roles(role)
            role2 = discord.utils.find(lambda r: r.name == 'Member', msg.guild.roles)
            await user.add_roles(role2)
            role3 = discord.utils.find(lambda r: r.name == 'New', msg.guild.roles)
            await user.remove_roles(role3)
        if reaction.emoji == '💚' and msg.id == msgid:
            print('Monika role given')
            role = discord.utils.find(lambda r: r.name == 'Team Monika', msg.guild.roles)
            await user.add_roles(role)
            role2 = discord.utils.find(lambda r: r.name == 'Member', msg.guild.roles)
            await user.add_roles(role2)
            role3 = discord.utils.find(lambda r: r.name == 'New', msg.guild.roles)
            await user.remove_roles(role3)
        if reaction.emoji == '🅱' and msg.id == msgid:
            print('Protag role given')
            role = discord.utils.find(lambda r: r.name == 'Team Protag', msg.guild.roles)
            await user.add_roles(role)
            role2 = discord.utils.find(lambda r: r.name == 'Member', msg.guild.roles)
            await user.add_roles(role2)
            role3 = discord.utils.find(lambda r: r.name == 'New', msg.guild.roles)
            await user.remove_roles(role3)
        if reaction.emoji == '🕷' and msg.id == msgid:
            print('Amy role given')
            role = discord.utils.find(lambda r: r.name == 'Team Amy', msg.guild.roles)
            await user.add_roles(role)
            role2 = discord.utils.find(lambda r: r.name == 'Member', msg.guild.roles)
            await user.add_roles(role2)
            role3 = discord.utils.find(lambda r: r.name == 'New', msg.guild.roles)
            await user.remove_roles(role3)
        if reaction.emoji == '✅' and msg.id == msgid:
            print('ADBD role given')
            role = discord.utils.find(lambda r: r.name == 'Team ADBD', msg.guild.roles)
            await user.add_roles(role)
            role2 = discord.utils.find(lambda r: r.name == 'Member', msg.guild.roles)
            await user.add_roles(role2)
            role3 = discord.utils.find(lambda r: r.name == 'New', msg.guild.roles)
            await user.remove_roles(role3)

bot.run('NDQ5OTk4NjU4MjkzNzI3MjQz.Des1bg.Aley6Z9_iZBgbuQKHpSOXj4LWTo')
