# Invite link:  https://discordapp.com/oauth2/authorize?client_id=478762645428633612&scope=bot

import discord
from discord.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# client.say doesn't need to specify a channel like send_message,
# it simply sends it in the same channel as the command

@client.command()
async def sub(name):
    output = name;
    await client.say(output)

@client.command()
async def unsub(name):
    output = name;
    await client.say(output)

@client.command()
async def echo(*args):
    output = ""
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command()
async def help():

    embed = discord.Embed(title=" ", color=0xff8233)
    embed.set_author(name="Ramble Bot Help ")
    embed.add_field(name='!help', value='Shows this help menu', inline=False)
    await client.say(embed=embed)

client.run(TOKEN)
